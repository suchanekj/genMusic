from __future__ import division

# fittables
rhythm_split_11 = 0.8
patternNoteNumMul = 4
scaleWeights = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
jumpWeights = [  1,   1,   1,  1,  1,  1,  2,  2,  3,  3,  4,  4, 1, 4, 4, 3, 3, 2, 2, 1, 1, 1,  1,  1,  1]
minTone = -12
maxTone = 12
patternRhythmNum = 3
patternMelodyNum = 3
sameRhythmWeight = [1, 3, 2]  # as 1 ago, as 2 ago...
sameMelodyWeight = [0, 2, 1]  # as 1 ago, as 2 ago..., must be same length as sameRhythmWeight

#fittables ranges
rhythm_split_11Range = [0,1] # min, max-min
patternNoteNumMulRange = [1,7]
scaleWeightsRange = [0,10]
jumpWeightsRange = [0,10]
minToneRange = [-39,39]
maxToneRange = [0,48]
patternRhythmNumRange = [1,11]
patternMelodyNumRange = [1,11]
sameRhythmWeightRange = [0,10]
sameMelodyWeightRange = [0,10]

# fittables types

rhythm_split_11Type = float
patternNoteNumMulType = int
scaleWeightsType = float
jumpWeightsType = float
minToneType = int
maxToneType = int
patternRhythmNumType = int
patternMelodyNumType = int
sameRhythmWeightType = float
sameMelodyWeightType = float

# constants for now
channels = 1
instruments = [1]
patternLen = 4

# constants
overallLen = 48  # in number of whole notes
tone0 = 60
jumps =       [-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
scaleLen = len(scaleWeights)
minNoteLen = 1/16


# edit the probabilities to sum to 1
# jumpWeightsSum = sum(jumpWeights)
# for i in range(len(jumpWeights)):
#     jumpWeights[i] = jumpWeights[i] / jumpWeightsSum
#
# scaleWeightsSum = sum(scaleWeights)
# for i in range(len(scaleWeights)):
#     scaleWeights[i] = scaleWeights[i] / scaleWeightsSum

rhythm_split_31 = 1 - rhythm_split_11
jumpScaleWeights = []

# create jump probabilities
def init():
    global jumpScaleWeights
    scaleWeights3 = scaleWeights + scaleWeights + scaleWeights
    for i in range(maxTone - minTone + 1):
        jumpScaleWeights.append([a*b*(1 if i + c >= 0 and i + c + minTone <= maxTone else 0) for a,b,c in
                        zip(jumpWeights,scaleWeights3[((i+minTone) % scaleLen) : ((i+minTone) % scaleLen)+2*scaleLen+1], jumps)])
        jumpScaleWeightsSum = sum(jumpScaleWeights[i])
        # print("sum: " + repr(jumpScaleWeightsSum))
        # print("i: " + repr(i))
        for j in range(len(jumpScaleWeights[i])):
            # print(jumpScaleWeights[i][j])
            jumpScaleWeights[i][j] = jumpScaleWeights[i][j] / jumpScaleWeightsSum
