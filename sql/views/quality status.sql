CREATE OR REPLACE VIEW workspace.default.vw_quality_status AS
SELECT
    equipment_id,
    ROUND(quality_rate * 100, 2) AS quality_pct,
    CASE
        WHEN quality_rate >= 0.98 THEN 'PASS'
        ELSE 'FAIL'
    END AS status
FROM workspace.default.oee_metrics_gold;