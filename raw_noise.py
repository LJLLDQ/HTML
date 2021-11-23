




# 注意这是log后的数据，应用时要解回来 例如math.exp(1.2)

# cam_noisy_params['NikonD850'] = {
#                                   'Kmin':1.2, 'Kmax':2.6, 'lam':-0.26, 'q':1/(2**14), 'wp':16383, 'bl':512,
#                                   'sigTLk':0.906, 'sigTLb':-0.6754,   'sigTLsig':0.035165,
#                                   'sigRk':0.8322,  'sigRb':-2.3326,   'sigRsig':0.301333,
#                                  }


# 
y = y * (p['wp'] - p['bl']) # 'wp':16383, 'bl':512
y = y / p['ratio'] # p的比例

# -------------------------------------------------------------------------- 添加shot noise部分 --------------------------------------------------------------------------
if use_P:   # 使用泊松噪声作为shot noisy    (光子散粒噪声)
    noisy_shot = np.random.poisson(y/p['K']).astype(np.float32) * p['K'] # 'Kmin':1.2, 'Kmax':2.6
else:   # 不考虑shot noisy那就采取随机噪声了
    noisy_shot = y + np.random.randn(*y.shape).astype(np.float32) * np.sqrt(np.maximum(y/p['K'], 1e-10)) * p['K']   # 'Kmin':1.2, 'Kmax':2.6

# -------------------------------------------------------------------------- 添加读噪声(read noise) --------------------------------------------------------------------------
if use_TL:   # 使用 Tukey lambda distribution噪声作为read noisy，里面包含 thermal noise, source follower, banding pattern
    noisy_read = stats.tukeylambda.rvs(p['lam'], scale=p['sigTL'], size=y.shape).astype(np.float32) # lam:-0.2, sigTL有三个值，'sigTLk':0.906, 'sigTLb':-0.6754,   'sigTLsig':0.035165,
else:   # 使用高斯噪声作为read noisy
    noisy_read = stats.norm.rvs(scale=p['sigGs'], size=y.shape).astype(np.float32) # sigGs 高斯噪声

# noisy_row行噪声
noisy_row = np.random.randn(y.shape[-2], 1).astype(np.float32) * p['sigR'] # sigR同样有三个 'sigRk':0.8322,  'sigRb':-2.3326,   'sigRsig':0.301333
noisy_q = np.random.uniform(low=-0.5*p['q'], high=0.5*p['q'], size=y.shape) * (p['wp'] - p['bl']) # 'q':1/(2**14), 'wp':16383, 'bl':512

z = (noisy_shot + noisy_read + noisy_row + noisy_q + p['bias']) / (p['wp'] - p['bl']) # 'wp':16383, 'bl':512, 偏移值bias