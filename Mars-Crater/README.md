### Project Overview

 This dataset was generated using HRSC nadir panchromatic image h0905_0000 taken by the Mars Express spacecraft. The images is located in the Xanthe Terra, centered on Nanedi Vallis and covers mostly Noachian terrain on Mars. The image had a resolution of 12.5 meters/pixel. The problem at hand is to determine if the instance is a crater or not a crater. Where 1=Crater, and 0=Not Crater


### Learnings from the project

 Using the technique described by L. Bandeira (Bandeira, Ding, Stepinski. 2010.Automatic Detection of Sub-km Craters Using Shape and Texture Information) we identify crater candidates in the image using the pipeline depicted in the figure below. Each crater candidate image block is normalized to a standard scale of 48 pixels. Each of the nine kinds of image masks probes the normalized image block in four different scales of 12 pixels, 24 pixels, 36 pixels, and 48 pixels, with a step of a third of the mask size (meaning 2/3 overlap). We totally extract 1,090 Haar-like attributes using nine types of masks as the attribute vectors to represent each crater candidate. The dataset was converted to the Weka ARFF format by Joseph Paul Cohen in 2012.
We construct a attribute vector for each crater candidate using Haar-like attributes described by Papageorgiou 1998. These attributes are simple texture attributes which are calculated using Haar-like image masks that were used by Viola in 2004 for face detection consisting only black and white sectors. The value of an attribute is the difference between the sum of gray pixel values located within the black sector and the white sector of an image mask. The figure below shows nine image masks used in our case study. The first five masks focus on capturing diagonal texture gradient changes while the remaining four masks on horizontal or vertical textures.


### Approach taken to solve the problem

 The approaches used in this project are:
1. ROC Score
2. Decision Tree
3. Random Forest Classifier
4. Bagging and Bootstrap Aggregation 
5. Voting Classifier



