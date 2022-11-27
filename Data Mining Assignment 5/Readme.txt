1.Locality sensitive Hashing : LSH.ipynb

Implemented Locality Sensitive Hashing from scratch, the dataset used here is 3 sentences of my own with words(this helped me understand), from which singles are generated. Then the vocabulary of all shingles is generated. Techniques such as One-hot encoding, Min-hashing, finding jaccard distance are used. Buckets are then created, filled with signatures and candidate pairs are found and returned which denote similarity between a pair of text.

2. Random projections : Random Projections.ipynb

Implemented Random projections from scratch, the dataset used is my own 2d array. 3 hyperplanes with 2 dimensions are used. Dot product is used to calculate the positive and negative side of the hyperplane. Then int array is converted to string, buckets are created and vectors are added to it. The values in the same buckets denote similarity.


3. Using FAISS and Annoy library to implement the following:

- Exhaustive search (Exhaustive_search.ipnb)
- Product quantization (Product_quantization.ipynb)
- Trees and graph (Trees_and_Forests.ipynb_
- HNSW methods (HNSW_Nearest_neighbor_FAISS.ipynb)
(Nearest_neighbor_FAISS) - just experimenting with this libraries 
The above methods are used with datasets(from github) to find the nearest neighbors.
