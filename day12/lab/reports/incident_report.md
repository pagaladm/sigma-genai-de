# Incident Report

## 1. Summary
An incident occurred due to schema drift where the column `merchant_name` was incorrectly renamed to `merchant_nm`. This resulted in data discrepancies and required immediate action to rectify the issue. A total of 100 records were affected, and GMV (Gross Merchandise Volume) impact analysis was completed. All affected records have been successfully recovered by renaming the column back to `merchant_name`.

## 2. Root Cause
The root cause of this incident was identified as **Schema Drift**. Specifically, the column `merchant_name` was inadvertently renamed to `merchant_nm`, leading to data inconsistencies.

## 3. Business Impact
- **Records Affected**: 100
- **GMV Impact Analysis**: Completed

The incident led to temporary data inconsistencies, impacting 100 records. A GMV impact analysis was conducted to assess the financial implications, which confirmed the need for immediate recovery actions.

## 4. Recovery Actions
- **Records Fixed**: 100
- **Actions Taken**: 
  - The column `merchant_nm` was renamed back to `merchant_name`.
  - All affected records were reviewed and corrected.
- **Outcome**: Recovery was successful, and data integrity was restored.

## 5. Prevention Recommendations
To prevent future incidents of schema drift, the following recommendations are proposed:
- **Automated Schema Validation**: Implement automated checks to validate schema changes before they are applied.
- **Change Management**: Establish a formal change management process for database schema modifications.
- **Regular Audits**: Conduct regular audits of the database schema to identify and rectify drifts early.
- **Training**: Provide training for database administrators on the importance of schema consistency and the proper procedures for making changes.