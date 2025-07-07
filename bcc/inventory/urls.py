from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [

    # http://localhost:8000/inventory/home/
    path('home/', views.home, name = 'home'),

    # http://localhost:8000/inventory/refresh-tires/
    path('refresh-tires/', views.refresh_tires, name = "refresh-tires"),

    # http://localhost:8000/inventory/refresh-magwheels/
    path('refresh-magwheels/', views.refresh_magwheels, name = "refresh-magwheels"),

    # http://localhost:8000/inventory/tires/
    path('tires/', views.viewAllTires, name = "all-tire-transaction"),

    # http://localhost:8000/inventory/tires/summary/
    path('tires/summary/', views.viewSummaryTires, name = "summary-tire-transaction"),

    # http://localhost:8000/inventory/tire-transaction/query/
    path('tire-transaction/query/', views.queryTireTransaction, name = "query-tire-transaction"),

    # http://localhost:8000/inventory/tire-transaction/create/
    path('tire-transaction/create/', views.createTireTransaction, name = "create-tire-transaction"),

    # http://localhost:8000/inventory/tire-transaction/edit/1/
    path('tire-transaction/edit/<int:pk>/', views.editTireTransaction, name = "edit-tire-transaction"),

    # http://localhost:8000/inventory/tire-transaction/delete/1/
    path('tire-transaction/delete/<int:pk>/', views.deleteTireTransaction, name = "delete-tire-transaction"),

    # http://localhost:8000/inventory/magwheels/
    path('magwheels/', views.viewAllMagwheels, name = "all-magwheel-transaction"),

    # http://localhost:8000/inventory/magwheels/summary/
    path('magwheels/summary/', views.viewSummaryMagwheels, name = "summary-magwheel-transaction"),

    # http://localhost:8000/inventory/magwheel-transaction/query/
    path('magwheel-transaction/query/', views.queryMagwheelTransaction, name = "query-magwheel-transaction"),

    # http://localhost:8000/inventory/magwheel-transaction/create/
    path('magwheel-transaction/create/', views.createMagwheelTransaction, name = "create-magwheel-transaction"),

    # http://localhost:8000/inventory/magwheel-transaction/edit/1/
    path('magwheel-transaction/edit/<int:pk>', views.editMagwheelTransaction, name="edit-magwheel-transaction"),

    # http://localhost:8000/inventory/magwhee;-transaction/delete/1/
    path('magwheel-transaction/delete/<int:pk>/', views.deleteMagwheelTransaction, name = "delete-magwheel-transaction"),

    # http://localhost:8000/inventory/masterlist/
    path('masterlist/', views.viewMasterlist, name = "masterlist"),

    # http://localhost:8000/inventory/full-transaction-form/
    path('full-transaction-form/', views.fullTransactionView, name = "full-transaction-view"),

    path('v2/transaction/create/', views.v2_create_transaction, name = "v2-create-transaction"),
    path('v2/transaction/save-draft/', views.v2_save_transaction_draft, name='v2-save-transaction-draft'),
    path('v2/transaction/cancel/', views.v2_cancel_transaction, name="v2-cancel-transaction"),
    path('v2/transaction/all/', views.v2_viewAllTransactions, name = 'v2-view-all-transactions'),
    path('v2/transaction/expand/<int:pk>', views.v2_expandTransaction, name = 'v2-expand-transaction'),
    path('v2/transaction/edit/<int:pk>', views.v2_editTransaction, name = 'v2-edit-transaction'),
    path('v2/transaction/delete/<int:pk>', views.v2_deleteTransaction, name = 'v2-delete-transaction'),

    path('v2/transaction/tire/add/', views.v2_addTire, name = "v2-add-tire"),
    path('v2/transaction/tire/edit/<int:index>/', views.v2_addTire, name = "v2-edit-tire"),
    path('v2/transaction/tire/delete/<int:index>/', views.v2_deleteTire, name = "v2-delete-tire"),
    path('v2/tires/', views.v2_viewAllTires, name = "v2-view-all-tires"),
    path('v2/tires/edit/<int:pk>/', views.v2_editSavedTire, name = "v2-edit-saved-tire"),
    path('v2/tires/delete/<int:pk>/', views.v2_deleteSavedTire, name='v2-delete-saved-tire'),
    path('v2/tires/summary/', views.v2_viewSummaryTires, name="v2-view-summary-tires"),
    path('v2/tires/query/', views.v2_queryTires, name="v2-query-tires"),
    
    path('v2/transaction/magwheel/add/', views.v2_addMagwheel, name = "v2-add-magwheel"),
    path('v2/transaction/magwheel/edit/<int:index>/', views.v2_addMagwheel, name = "v2-edit-magwheel"),
    path('v2/transaction/magwheel/delete/<int:index>/', views.v2_deleteMagwheel, name = "v2-delete-magwheel"),
    path('v2/magwheels/', views.v2_viewAllMagwheels, name = "v2-view-all-magwheels"),
    path('v2/magwheels/edit/<int:pk>/', views.v2_editSavedMagwheel, name = "v2-edit-saved-magwheel"),
    path('v2/magwheels/delete/<int:pk>/', views.v2_deleteSavedMagwheel, name='v2-delete-saved-magwheel'),
    path('v2/magwheels/summary/', views.v2_viewSummaryMagwheels, name="v2-view-summary-magwheels"),
    path('v2/magwheels/query/', views.v2_queryMagwheels, name="v2-query-magwheels"),

    path('v2/transaction/payment/add/', views.v2_addPayment, name = "v2-add-payment"),
    path('v2/transaction/payment/edit/<int:index>/', views.v2_addPayment, name = "v2-edit-payment"),
    path('v2/transaction/payment/delete/<int:index>/', views.v2_deletePayment, name = "v2-delete-payment"),
    path('v2/transaction/<int:transaction_id>/payment/edit/<int:pk>/', views.v2_editSavedPayment, name = "v2-edit-saved-payment"),

    path('v2/reports/payments/', views.v2_paymentReportView, name = "v2-payment-report-view"),
    path('v2/reports/payments/export/', views.v2_paymentReportExport, name = "v2-payment-report-export"),



]