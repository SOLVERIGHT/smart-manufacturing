CREATE OR REPLACE VIEW workspace.default.vw_downtime_by_equipment AS
SELECT
    equipment_id,
    downtime_minutes
FROM workspace.default.oee_metrics_gold;