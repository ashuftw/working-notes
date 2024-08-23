Status: #finished 
### Use case 
Evidence is neither measured or modeled. However one can calculated using the numerator of the [[240401 Bayes Theorem|Bayes Theorem]]. 
$$\boxed{
C =\sum_{i \in \mathcal{S}} p(\mathbf{x} \mid s=i) \cdot P(s=i)
}$$

### Derivation
Using the [[240410 Bayes Classifier|Bayes Classifier]]

$$\sum_{i \in \mathcal{S}} P(s=i \mid \mathbf{x}) = \sum_{i \in \mathcal{S}} \frac{p(\mathbf{x} \mid s=i) P(s=i)}{p(\mathbf{x})} = 1$$
Separating $RHS$
$$
1  = \sum_{i \in \mathcal{S}} \frac{p(\mathbf{x} \mid s=i) P(s=i)}{p(\mathbf{x})}$$
Multiply $p(x)$ on both sides
$$
\sum_{i \in \mathcal{S}} {p(\mathbf{x})}  =  \sum_{i \in \mathcal{S}} p(\mathbf{x} \mid s=i) P(s=i)
$$
Evidence $C$
$$\boxed{
C =  \sum_{i \in \mathcal{S}} p(\mathbf{x} \mid s=i) P(s=i)
}$$


> Note: Here $S$ is the class, $\mathbf x$ is the feature vector that can be used to make the classification. 







---
# References
