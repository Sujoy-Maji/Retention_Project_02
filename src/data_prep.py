# Initialize data preparation for hotel bookings
import pandas as pd
import numpy as np
# Handling missing values: agent and company IDs
# Outlier treatment: Capping extreme ADR (Average Daily Rate) values
# Feature Engineering: Total duration of stay
df['total_stay'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
