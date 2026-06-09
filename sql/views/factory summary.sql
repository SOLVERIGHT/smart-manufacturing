CREATE OR REPLACE VIEW workspace.default.vw_factory_summary AS
SELECT
    ROUND(
        SUM(good_count) / SUM(total_count),
        4
    ) AS overall_quality_rate,
    SUM(total_count) AS total_production,
    SUM(defect_count) AS total_defects,
    SUM(downtime_minutes) AS total_downtime
FROM workspace.default.oee_metrics_gold;