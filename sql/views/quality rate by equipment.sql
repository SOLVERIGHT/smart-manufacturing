CREATE OR REPLACE VIEW workspace.default.vw_quality_by_equipment AS
SELECT
    equipment_id,
    quality_rate
FROM workspace.default.oee_metrics_gold;