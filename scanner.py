from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
from scipy import spatial
from sklearn.metrics import pairwise_distances
import scipy.stats
sample_rate, data = read("sezenseries.wav")
sample_ratee, dataa = read("sezenintro.wav")

print("The sample rate is: " + str(sample_rate) + " samples per seconds.")
print("There are " + str(len(data))+" samples")
print("Then the audio should last: " + str(len(data)/sample_rate) + " seconds")


print("The sample rate is: " + str(sample_ratee) + " samples per seconds.")
print("There are " + str(len(dataa))+" samples")
print("Then the audio should last: " + str(len(dataa)/sample_ratee) + " seconds")

#series = np.array(data)
#series = series.flatten()
#print(series.shape)



cnt = 0
best_corr = -1
best_pos = 0
while True:
    if cnt > 180*sample_rate:
        break
    if cnt + dataa.shape[0] > data.shape[0]:
        break
    # corr = np.corrcoef(data[cnt:cnt + dataa.shape[0]], dataa)

    # corr, _ = scipy.stats.spearmanr(np.sum(data[cnt:cnt + dataa.shape[0]], axis=1), np.sum(dataa, axis=1))
    corr = 1 - spatial.distance.cosine(np.sum(data[cnt:cnt + dataa.shape[0]], axis=1), np.sum(dataa, axis=1))
    if abs(corr) > best_corr:
        best_corr = abs(corr)
        best_pos = cnt
    cnt += sample_rate

print(f"INTRO starts in  {best_pos/sample_rate} and ends in {(best_pos+dataa.shape[0])/sample_ratee}")
