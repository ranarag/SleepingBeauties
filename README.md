# SleepingBeauties
Implementation of the method described in the paper "Sleeping Beauties in Computer Science: Characterization and Early Identification"

**sleepingBeauty.py** is used for finding the ids of sleeping beauties from a given corpus.

### How to Run
*python sleepingBeauty.py <inputFile>*

where **inputFile** contains the citation profile of papers in the form:
<paper_id>:<enter>
<comma separated list of citation counts received by the paper in the consecutive years from its year of publication>

#### Example
50331648:  **<----- id of the paper**
0,0,3,2,2,1,0,0,1, **<--------citation received by the paper in the first year = 0, in second year =0, in third year = 3, and so on**

The results could be found in the file **sb_ids.txt** where each line will represent an id of a paper which is supposed to be a sleeping beauty