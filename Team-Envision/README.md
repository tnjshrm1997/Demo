# Stammer.io

# Team Envision

# Problem Statement

More than 70 million people worldwide are stutterers that’s one in every 100.
Past few years have seen an increase in popularity of personal voice assistants which can actually speed up the day to day tasks. But that is limited by the ability of the speaker. If the input to the voice recognition system is from a stutterer, it fails miserably with accuracy as low as 18% and as high as 73% as compared to a baseline of 92% for normal speaker. So our project aims to correct the Speech-to-Text conversion for a stuttered speech.

# Abstract

The existing work that has been done for this problem is just classification of a speech as a stuttered speech or a normal speech.
It’s observed, that when a person stutters, there is a decrease in the amplitude in the person’s voice signal and we used this, to eliminate the repetitions, elongations and silent intervals to produce a better speech recognition system.
The aim of this project is to come up with a new machine learning algorithm to enhance speech recognition for people suffering from stuttering and implementing it on Web and Android App. The basic idea is to first remove stuttering from the sample by using the amplitude threshold obtained from neural networks and then passing the clean sample through IBM Watson's Speech-to-text which already has a trained model for GB English obtaining.



