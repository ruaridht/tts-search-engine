# TTS Practical
Ruaridh Thomson

## Specification
Your goal is to develop a search engine for retrieving relevant images in response to keyword queries. To aid in the development, you are provided with a set of 40 training queries, a set of relevance judgments, and software for evaluating the accuracy of your algorithms. Your algorithms will be tested on a different set of 40 testing queries, for which no relevance judgments will be available. Please familiarize yourself with the Data and Formats section, and then complete the following steps:
* Implement a simple word overlap retrieval algorithm. Your implementation should read the query file (a2.qrys) and the document file (a2.docs). Then, for each query Q and for each document D count how many distinct words are present in both Q and D (lecture 4, slide 5, second equation). Print all counts into a file as described in the search results section below. Run this algorithm over the original documents in a2.docs, i.e. without trying to improve performance. Save the results in a file called overlap.top.
* Implement a tf.idf retrieval algorithm, based on the weighted sum formula with tf.idf weighting (lecture 4, slide 8, set k=2). Document frequency for a given word should be computed by counting the number of distinct images that contain this word. Run this algorithm over the original documents in a2.docs, i.e. without trying to improve performance. Save the results in a file called tfidf.top as described in the search results section below.
* Try to improve the accuracy of your retrieval algorithms. You are free to use any techniques and any pre-processing steps that you think may improve retrieval effectiveness. Use average precision (see below) to judge the accuracy of your approach. Save the results of your most successful algorithm in a file called best.top. Come up with a short distinctive name for your algorithm and save it in a file called best.id. This name will be used when we report the effectiveness of your algorithm.
* Evaluate the performance of your algorithms, using the provided trec_eval program. You can do this on a Linux command line by running: 
     trec_eval -o -c -M1000 a2.qrel overlap.top 
     trec_eval -o -c -M1000 a2.qrel tfidf.top 
     trec_eval -o -c -M1000 a2.qrel best.top 
The program will print 11 standard recall/precision points, as well as average precision, R-precision, and precision at fixed ranks (details provided in lecture 8). Create an 11-point recall-precision plot which contains three curves: one for word overlap, one for tf.idf and one for your best algorithm.
* Run your best retrieval algorithm from task 3 on the set of testing queries (test.qrys). Average precision (MAP) of your algorithm will be used as the main criterion for marking this task. You can assume that MAP over the training queries will be representative of the MAP over the testing queries. Save the result as test.top, and be sure to use exactly the format described in the search results section.
* Provide a 1-page report outlining the decisions you made in implementing the search algorithm, as well as your comments on the relative performance of the algorithms you tried. Discuss the significance of your results. Include the recall-precision plot from task 4 in the report (can be on a separate page). Save the file as report.pdf.

## Notes
The following regular expression may be useful for matching tags: <[^>]*>
You should only follow anchor tags of the form: <a ...> ... </a>
You should not follow any links pointing outside of the Informatics network.