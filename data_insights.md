# Data Insights 
Our aim is to uncover insights into customer satisfaction, delivery efficiency, and purchasing patterns through statistical analysis, machine learning, and data visualization.

## Analyzed Questions
- **Sales Trends Over Time**: Identifying periods of high demand to inform inventory and marketing strategies.
- **Popular Product Categories**: Highlighting top-selling categories to prioritize stock and marketing efforts.
- **Geographic Distribution of Sales**: Tailoring logistics strategies to improve delivery times in key markets.
- **Influence of Payment Types on Purchases**: Enhancing the checkout process to increase conversion rates.
- **Customer Satisfaction Distribution**: Identifying improvement areas in product quality, service, and delivery.
- **Factors Affecting Delivery Times**: Analyzing and optimizing delivery performance to reduce late deliveries.
- **Time to Delivery vs. Customer Satisfaction**: Examining the impact of delivery times on satisfaction levels.
- **Key Predictors of Customer Satisfaction**: Using machine learning to focus efforts on aspects crucial to customers.
- **Actual vs. Estimated Delivery Times**: Assessing delivery estimate accuracy and its satisfaction impact.
- **Strategies for Business Improvement**: Formulating recommendations based on data insights to enhance customer experience and business performance.

### Types of customer behavior 
1. **Complex:** occurs when customers invest significant time and effort in evaluating products before making a purchase. High-involvement products, such as cars or expensive electronics, often trigger this type of behavior.
2. **Dissonance-reducing**: takes place when customers experience post-purchase anxiety or uncertainty about their decision. This can arise when consumers feel that they had to make a decision quickly, without sufficient time to weigh the pros and cons, or if their choice was informed by limited information.
3. **Habitual buying:** characterized by consumers relying on routines and habits when making purchasing decisions. This type of behavior is commonly found in less involving product categories, such as groceries or personal care items, where consumers are not as inclined to research products extensively before purchase. 
4. **Variety seeking:** arises when customers actively seek new experiences, products, or brands, even if satisfied with their current choices. This behavior typically occurs in categories where products are low-involvement, low-cost commodities, and consumers feel minimal risk in trying new options.

### Factors that Influence Customer Behavior
1. **Demographic**
2. **Psychographic**
3. **Social**
4. **Cultural**
5. **Economical**

The following code addresses all of these, given a dataset and the following hypothesis: 

- We will not work with deep learning as it does not provide insights into the patterns. <- no explainability.We will also conclude with an analysis in explainability. 
- We will work with regression and likeability (⁠xgboost regressor e classification)- and ARIMA for qualitative prediction.
- Qualitative data analysis must also identify outliers 
- If too many features, proceed with [feature selection](https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/)
- Check for class imbalance: If one class is much less frequent than others, traditional accuracy may not be a good indicator of performance.
- Use appropriate metrics: Consider using F1 score or precision instead of accuracy to evaluate your model, especially for the underrepresented class.
- Visualize performance: Creating an ROC curve helps to understand the trade-offs between true positive and false positive rates across different threshold settings. 
- We will validate the model with bootstrap if there is time. 
- Use library [SHAP](https://shap.readthedocs.io/en/latest/index.html) 
- Using XGboost, we will make analysis of feature importance, which derive from feature trees
- Clustering will be done in the end


### Step by step
1. Clean data
2. Correlation study among variables using phil metric for categorical, pearson for numerical
3. Data standardization 
4. Initial screening (feature selection for numerical using standard deviation, and xquadro for categorical)
5. Secondary screening (onehot encoding and fisher scores)
6. Divide test and train set (random oversampling if needed)
7. Clustering alghorithm + qualitative analysis + feature selection + look for outliers 
8. ARIMA
9. XGBoost Algorithm 
10. ROC and A curve
11. Plotting and conclusions 

## Important to say

"Predictive machine learning models like XGBoost become even more powerful when paired with interpretability tools like SHAP. These tools identify the most informative relationships between the input features and the predicted outcome, which is useful for explaining what the model is doing, getting stakeholder buy-in, and diagnosing potential problems. It is tempting to take this analysis one step further and assume that interpretation tools can also identify what features decision makers should manipulate if they want to change outcomes in the future. However, in this article, we discuss how using predictive models to guide this kind of policy choice can often be misleading.

The reason relates to the fundamental difference between correlation and causation. SHAP makes transparent the correlations picked up by predictive ML models. But making correlations transparent does not make them causal! All predictive models implicitly assume that everyone will keep behaving the same way in the future, and therefore correlation patterns will stay constant. To understand what happens if someone starts behaving differently, we need to build causal models, which requires making assumptions and using the tools of causal analysis."


