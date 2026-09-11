# Learning points

<h2>Correlation Analysis: Discovering the Strength of Associations</h2>

<h3>Interpreting Pearson Correlation Coefficient</h3>

<li>There is a <b>strong positive correlation</b> (0.64) between 'floor_area_sqm' and 'resale_price', suggesting that larger floor areas are associated with higher resale prices.</li>

<li>There is a <b>moderate positive correlation</b> (0.34) between 'lease_commence_date' and 'resale_price', indicating that properties with longer remaining leases tend to have higher resale prices.</li>

<br>
<h3>Limitations of Pearson Correlation Coefficient</h3>

<h4>Designed for Continuous Variables</h4>

<p>
You may have realised that we only implemented Pearson correlation with the continuous variables in the data. This is because Pearson correlation is specifically designed for use with continuous variables. Pearson correlation uses the mean to calculate how each data point deviates from the average, which is essential for determining the linear relationship between the variables. This calculation assumes that the data points are continuous and can take on any value within a range, making the mean a meaningful and informative measure.

Using Pearson correlation with other types of variables, such as ordinal or categorical variables, can lead to misleading or incorrect results. Ordinal or categorical variables do not have a meaningful average in the same way continuous variables do. For example, averaging ranks or categories can lead to misleading interpretations, as these data types represent distinct, non-numeric differences rather than a continuum of values.
</p>
<br>
<h4>Linear Relationship Assumption</h4>

<p>
Pearson's correlation assumes that the relationship between the variables is linear. It may not accurately capture the strength or direction of non-linear relationships. For example, a perfect quadratic relationship may result in a low Pearson correlation coefficient.
</p>

<h4>Normality Assumption</h4>

<p>
The Pearson correlation assumes that the data is normally distributed. When this assumption is violated, the correlation coefficient may not accurately reflect the true relationship between the variables.
</p>
<h4>Homogeneity of Variance</h4>

<p>
Pearson's correlation assumes that the spread or variance of the data points is constant across the entire range of values (this is called homoscedasticity). Think of it like having a basketball court where the floor is perfectly flat.

If the floor is flat, it is easy to measure distances accurately. However, if the floor has bumps and dips (this is called heteroscedasticity), measuring distances becomes tricky and unreliable.

Similarly, when data points have different spreads at different levels, the correlation measurement might not be accurate. When the data shows heteroscedasticity (i.e., the variance changes at different levels of the variables), it would be like trying to measure straight-line distances on a bumpy surface – your results might not truly represent the reality.
</p>

<h4>Sensitivity to Outliers</h4>

<p>
Pearson's correlation is sensitive to outliers. Extreme values can disproportionately influence the correlation coefficient, leading to misleading results. Even a few outliers can significantly distort the measure of the overall relationship between the variables.
</p>


<h3>Interpreting Spearman Rank Correlation Coefficient</h3>

<p>
<li>There is a <b>strong positive monotonic correlation</b> between the 'floor_area' and the 'resale_price'. Larger flats tend to have higher resale prices, and this relationship is relatively strong. </li>

<li>There is a <b>moderate positive monotonic relationship</b> between the 'lease_commence_date' and the 'resale_price'. Flats with more recent lease commencement dates tend to have higher resale prices. </li>

<li>There is a <b>weak positive monotonic correlation</b> between the 'storey_range' and the 'resale_price'. Higher storey flats tend to have higher resale prices, but the relationship is not strong.</li>
</p>

<h3>Limitations of Spearman Rank Correlation Coefficient</h3>

<h4>Assumes Ordinal, Interval or Ratio Data</h4>

<p>
Spearman correlation requires that the data be at least ordinal. It is not suitable for nominal data, where there is no inherent order.
</p>

<h4>Only Measures Monotonic Relationships</h4>

<p>
Spearman correlation assesses the strength of monotonic relationships. If the relationship between variables is not monotonic (i.e., it changes direction), Spearman correlation may not capture the true nature of the relationship.</p>

<h4>Insensitive to Linear Relationships</h4>

<p>
Spearman correlation might indicate a high correlation for non-linear but monotonic relationships. Conversely, it might not detect a strong linear relationship if it is not perfectly monotonic. In cases where the relationship is specifically linear, Pearson correlation might be more appropriate.</p>

<h4>Rank-based Approach</h4>

<p>
Since Spearman correlation is based on ranks, it ignores the actual magnitudes of the values. This can lead to loss of information, especially if the magnitude of differences between values is important. Tied ranks (identical values in the data) can affect the accuracy of the Spearman correlation coefficient. While Spearman's method can handle ties by assigning average ranks, extensive ties can still distort the correlation coefficient.</p>

<h4>Less sensitivity to Distribution</h4>

<p>
Spearman correlation does not take into account the distribution of the data. If the data have outliers or are skewed, it might not accurately reflect the relationship between the variables. Since Spearman correlation uses ranks rather than the actual values themselves, the influence of outliers is minimised. An outlier's rank will still be an extreme value, but it does not affect the overall calculation as much as in Pearson correlation. Therefore, Spearman correlation is less affected by outliers compared to Pearson correlation.

While being less sensitive to outliers and skewness can be an advantage, it can also be a drawback. If the outliers or the skewness are meaningful parts of the data (e.g., indicating a particular trend or anomaly), Spearman correlation might underrepresent their impact on the relationship between variables.</p>

<h2>When to Use Normalization</h2>
<li><b>Distance-Based Algorithms:</b> Algorithms that rely on distance calculations, such as k-Nearest Neighbors (k-NN) and k-means clustering, benefit greatly from normalization. If features are on different scales, those with larger ranges can disproportionately influence the distance calculations. By normalizing the features, each one contributes equally, ensuring a more balanced and accurate computation of distances.</li>

<li><b>Gradient Descent Optimization:</b> For models like neural networks and logistic regression that use gradient descent for optimization, normalization can significantly improve the training process. It speeds up the convergence of gradient descent, resulting in faster training times. This is because normalized data provides a more stable and efficient path towards the minimum of the loss function.</li>

<li><b>Equal Importance of Features:</b> When you want each feature to have the same impact on the outcome, normalization is essential. It ensures that no single feature dominates the model due to its scale, leading to a more balanced contribution from all features.</li>

<h2>When to Use Standardization</h2>
<li><b>Algorithms Assuming Normal Distribution:</b> Algorithms like linear regression and linear discriminant analysis assume that the input features are normally distributed. Standardization helps in meeting this assumption by centering the features around the mean and scaling them to have a standard deviation of one.</li>

<li><b>Distance-Based Algorithms:</b> Similar to normalization, standardization benefits distance-based algorithms like k-Nearest Neighbors (k-NN) and k-means clustering. Standardizing features ensures that each one contributes equally to the distance calculations.</li>

<li><b>Gradient Descent Optimization:</b> For models optimized using gradient descent, such as neural networks, standardization can lead to faster convergence. This is because features with similar scales provide a more stable and efficient optimization path.</li>