prior_probability = 0.01
false_positive = 0.05
true_positive = 0.98
prior_complement = 1 - prior_probability
true_negative = 1 - false_positive
evidence = (true_positive * prior_probability) + (false_positive * prior_complement)
posterior_probability = (true_positive * prior_probability) / evidence
print(f"Prior Probability (P(Disease)): {prior_probability}")
print(f"False Positive Probability (P(Positive | No Disease)): {false_positive}")
print(f"True Positive Probability (P(Positive | Disease)): {true_positive}")
print(f"True Negative Probability (P(Negative | No Disease)): {true_negative}")
print(f"Evidence (P(Positive)): {evidence}")
print(f"Posterior Probability (P(Disease | Positive)): {posterior_probability:.4f}")
