---
title: CDMA code spreading demostrate with Python
---

This article will use a simple example to demostrate CDMA.

It will spreading a singal with PN code, then despreading it to recovery the signal.

<!-- more -->

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

plt.style.use('ggplot')

b = np.random.randint(2, size=8)
ln=len(b)

sig_len=8

bb=b.repeat(sig_len)
bbx=np.arange(sig_len*ln)
lens=len(bb)

# Signal Data
plt.figure(figsize=(8, 4.5))
plt.suptitle(r'Spreading')
plt.subplot(311)
plt.step(bbx,bb)
plt.title(r'Signal Data')

#PN Code
pr_sig=np.random.randint(2, size=lens)
plt.subplot(312)
plt.step(bbx,pr_sig)
plt.title(r'PN Code')

# Spread Signal
plt.subplot(313)
C=np.logical_xor(bb,pr_sig)
plt.step(bbx,C)
plt.title(r'Spread Signal')
plt.tight_layout()
plt.subplots_adjust(top=0.88)


## De-spreading data
plt.figure(figsize=(8, 4.5))
plt.suptitle(r'De-Spreading')
plt.subplot(311)
C=np.logical_xor(bb,pr_sig)
plt.step(bbx,C)
plt.title(r'Spread Signal')
plt.subplot(312)
plt.step(bbx,pr_sig)
plt.title(r'PN Code')
D=np.logical_xor(C,pr_sig)
plt.subplot(313)
plt.step(bbx,D)
plt.title(r'Signal Data')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

# De-spreading with wrong PN code
plt.figure(figsize=(8, 4.5))
plt.suptitle(r'De-spreading with wrong PN code')
plt.subplot(311)
plt.step(bbx,C)
plt.title(r'Spread Signal')
plt.subplot(312)
pr_sig_w=np.random.randint(2, size=lens)
plt.step(bbx,pr_sig_w)
plt.title(r'Pn Code')
D=np.logical_xor(C,pr_sig_w)
plt.subplot(313)
plt.step(bbx,D)
plt.title('Output data')

plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.show()
```


![](http://oozvwxvcz.bkt.clouddn.com//17-12-25/19760412.jpg)

![](http://oozvwxvcz.bkt.clouddn.com//17-12-25/92526869.jpg)

![](http://oozvwxvcz.bkt.clouddn.com//17-12-25/74089624.jpg)

