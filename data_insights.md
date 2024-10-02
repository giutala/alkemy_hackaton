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



