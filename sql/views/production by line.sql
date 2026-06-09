CREATE OR REPLACE VIEW workspace.default.vw_production_by_line AS
SELECT
    line_id,
    SUM(total_count) AS total_production
FROM workspace.default.oee_metrics_gold
GROUP BY line_id;