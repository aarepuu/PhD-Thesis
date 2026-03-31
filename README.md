<p align="center">
<img src="word_count.png">
</p>

# My Ph.D. thesis written in LaTeX

### Abstract

This PhD research explores more inclusive and participatory ways of designing data-driven, people-centred smart city tools that serve the needs of citizens. In contrast to passive participation through data, this research focuses on ways of using data and technology for bringing people together to address issues in the community, and to intervene in the public space. Through different case studies I explore the role of data in civic participation and advocacy, focusing on active participation through data and digital tools that support collaborative sensemaking of that data.

## Table of Contents

- [Introduction](Introduction/).....................................1
- [Chapter 1: Literature Review](Chapter1/).........................5
- [Chapter 2: Case Study I - Data Production](Chapter2/)............12
- [Chapter 3: Case Study I - Data Use](Chapter3/)....................25
- [Chapter 4: Case Study II - Data Access](Chapter4/)................39
- [Chapter 5: CDI Model](Chapter5/)..................................50
- [Chapter 6: Case Study III](Chapter6/).............................62
- [Chapter 7: Discussion](Chapter7/)..................................75
- [Chapter 8: Conclusions](Chapter8/)................................90
- [Appendix 1](Appendix1/)...........................................105
- [Appendix 2](Appendix2/)...........................................110
- [Appendix 3](Appendix3/)...........................................115

## Declaration

This thesis is in accordance with _Newcastle University's Guidelines for the Submission and Format of Theses_ found at https://www.ncl.ac.uk/students/progress/student-resources/PGR/Guideline%20for%20Submission%20and%20Format%20of%20Theses%20July%202019.pdf

```Template HAS NOT been check against the latest guidelines!```

This thesis is using a _Newcastle University template_ by André Catarino Guerra, available at https://github.com/AndreGuerra123/NUTT. Thanks for uploading the source on GitHub!

Also using some styles adapted from _CUED LaTeX template_ by Krishna Kumar, available at https://github.com/kks32/phd-thesis-template.

Added publications section to list all the publications related to the thesis.

Thesis was written in _Overleaf_ (https://www.overleaf.com/) platform, and then cloned here.

## Counting Words

To count words over time in Tex files use a _Git Count Words_ LateX script by Bastian Rieck, originally available at https://gist.github.com/Submanifold/d7b996492dc3020f2acea87b49cc54c3.


### to use it

```
$ ./word_count.sh
```

### to set writing goals

To set daily writing goals modify ```$daily_goal``` parameter in ```word_count.sh``` script and use today to run the script.

```
$ ./word_count.sh today
```

### to make graph

```
$ ./word_count.sh | ./makegraph.py
```


## Downloadable document

http://theses.ncl.ac.uk/jspui/handle/10443/5172
