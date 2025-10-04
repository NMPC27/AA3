
# CSURÖS Counter and Space-Saving Count

##  Overview

This project explores two mathematical algorithms used for approximate counting and efficient data representation: the **CSURÖS Approximate Counter** and the **Space-Saving Count**.  
Both methods aim to optimize performance and memory usage when working with large datasets, such as counting occurrences in text streams or analyzing frequency distributions.

The experiments were conducted using different text versions of _“The Tragedy of Othello, the Moor of Venice”_ in **English**, **French**, and **German**, focusing on the accuracy and efficiency of each algorithm.


##  Algorithms

###  CSURÖS Approximate Counter

A probabilistic counting algorithm based on **random sampling**.  
It estimates the number of distinct elements in a dataset without counting each occurrence, using a **binary exponent** and **d-bit significand**.

-   **Key idea:** uses probabilistic increments that depend on the parameter `d`.
    
-   **Accuracy:** improves with higher values of `d`.
    
-   **Best results:** achieved for `d ≥ 14`.
    

**Use cases:**

-   Large-scale data streams
    
-   Approximate frequency analysis
    
-   Statistical counting where exactness is not critical
    


###  Space-Saving Count

A method designed to reduce storage space while tracking the most frequent elements in a data stream.  
It maintains counts for only the top `k` elements, replacing the least frequent ones as new elements appear.

-   **Key idea:** maintain limited capacity (`k`) and update counts dynamically.
    
-   **Accuracy:** improves as `k` increases.
    
-   **Best results:** achieved for `k ≥ 10`.
    

**Use cases:**

-   Stream processing
    
-   Text frequency analysis
    
-   Memory-limited environments
    



##  Methodology

1.  **Datasets:**
    
    -   Text files of _“The Tragedy of Othello”_ in **English**, **French**, and **German**.
        
    -   All letters were capitalized and counted.
        
2.  **Counters Implemented:**
    
    -   **Exact Counter:** baseline using Python’s `collections.Counter()`.
        
    -   **CSURÖS Counter:** implemented with probabilistic updates controlled by parameter `d`.
        
    -   **Space-Saving Counter:** maintains counts of the top `k` most frequent letters.
        
3.  **Testing:**
    
    -   Each counter was tested **10 consecutive times**.
        
    -   Average values were calculated for performance comparison.


## Results Summary

|Counter|Parameter|Accuracy|Notes|
|----------------|-------------------------------|-----------------------------|--|
|Exact Counter|—|100%|Baseline for comparison|
|CSURÖS Counter|d = 2|❌ Poor accuracy|High error due to frequent probabilistic updates|
|CSURÖS Counter|d ≥ 12|✅ Good accuracy|Low error; better with higher `d`|
|Space-Saving Count|k = 3|❌ Poor accuracy|Insufficient capacity for all frequent letters|
|Space-Saving Count|k ≥ 10|✅ Good accuracy|Closely matches exact counts|

-   Most frequent letters were consistent across all three languages.
    
-   Detailed results and plots are available in the **`Counters.xlsx`** file.


##  Files

-   `main.py` – implementation of both counters and testing logic
    
-   `Counters.xlsx` – contains experimental results and charts
    
-   `Report.pdf` – full documentation and analysis
    



##  Conclusion

-   **CSURÖS Counter** performs well with larger `d` values and provides a fast, low-memory alternative for approximate counting.
    
-   **Space-Saving Count** effectively identifies the most frequent elements when `k` is large enough.
    
-   Both algorithms demonstrate a trade-off between **accuracy** and **resource efficiency**, making them suitable for **large-scale or real-time data processing**.
    



##  References

1.  [Csurös, M. (2009). Approximate Counting in Data Streams. _arXiv:0904.3062_](https://arxiv.org/pdf/0904.3062.pdf)
    
2.  Amazon Romania – Data Streams Algorithms Presentation
    
3.  Teacher Lecture Slides
    



##  Author

**Nuno Cunha** – Student ID 98124  
3rd Project: _CSURÖS Counter and Space-Saving Count_
