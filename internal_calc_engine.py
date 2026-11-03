# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(gross_booking_revenue, property_maintenance_outlays, cleaning_turnover_costs):
    total_system_expense = float(property_maintenance_outlays) + float(cleaning_turnover_costs)
    gross_revenue = float(gross_booking_revenue)
    true_net_operational_margin = gross_revenue - total_system_expense
    return [gross_revenue, total_system_expense, true_net_operational_margin]
