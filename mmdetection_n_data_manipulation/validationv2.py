HB.TransactionValidationV2 = new function () {
    var IsNewProduct = false;
    var LineIndex = 0;
    var mx, my;

    //this.Init = function (Sender_Endpoint, Receiver_Endpoint, BillToParty, ShipToParty, SellToParty, SupplierParty, BillToVatNo, SellToVatNo, SupplierVatNo, BillToCompanyId, ShipToCompanyId, SellToCompanyId, SupplierCompanyId) {
    this.Init = function () {
        $(".select2").select2();
        if ($("#IsInValidFile").val() == "True") {
            sweetAlertInitialize();
            swal({
                title: $("#Message").val(),
                text: '',
                type: "error",
                confirmButtonColor: "#3498db",
                confirmButtonText: "Ok"
            },
           function () {
               window.location.href = '/DashBoard';
           });
        }
        $('.DeliveryDatePicker').datepicker();
        $('.input-group.date').datepicker({});
        //turn to inline mode
        //$.fn.editable.defaults.mode = 'popup';

        //HB.TransactionValidationV2.SetCountryList("SupplierParty_Country");
        //HB.TransactionValidationV2.SetCountryList("BillToParty_Country");
        //HB.TransactionValidationV2.SetCountryList("SellToParty_Country");
        //HB.TransactionValidationV2.SetCountryList("ShipToParty_Country");

        //HB.TransactionValidationV2.Set_Qualifier("SupplierParty_RegNo");

        //HB.TransactionValidationV2.ApplyXEditableToField();
        //HB.TransactionValidationV2.ApplyXEditableToParty("Sender_Endpoint", Sender_Endpoint);
        //HB.TransactionValidationV2.ApplyXEditableToParty("Receiver_Endpoint", Receiver_Endpoint);
        //HB.TransactionValidationV2.ApplyXEditableToParty("BillToParty_RegNo", BillToParty);
        //HB.TransactionValidationV2.ApplyXEditableToParty("ShipToParty_RegNo", ShipToParty);
        //HB.TransactionValidationV2.ApplyXEditableToParty("SellToParty_RegNo", SellToParty);
        //HB.TransactionValidationV2.ApplyXEditableToParty("SupplierParty_RegNo", SupplierParty);
        //HB.TransactionValidationV2.ApplyXEditableToParty("BillToParty_VATNo", BillToVatNo);
        //HB.TransactionValidationV2.ApplyXEditableToParty("SellToParty_VATNo", SellToVatNo);
        //HB.TransactionValidationV2.ApplyXEditableToParty("SupplierParty_VATNo", SupplierVatNo);
        //HB.TransactionValidationV2.ApplyXEditableToParty("BillToParty_CompanyId", BillToCompanyId);
        //HB.TransactionValidationV2.ApplyXEditableToParty("ShipToParty_CompanyId", ShipToCompanyId);
        //HB.TransactionValidationV2.ApplyXEditableToParty("SellToParty_CompanyId", SellToCompanyId);
        //HB.TransactionValidationV2.ApplyXEditableToParty("SupplierParty_CompanyId", SupplierCompanyId);


        $("input[name=Customer_Order_No]").focusout(function () {
            var str = $("input[name='Customer_Order_No']").val();
            if (str.length >= 6) {
                str = str.toLowerCase().replace("ao", '');
                if (str >= 2000 && str <= 9999) {


                    $("input[name='BillToParty.ContactRole']").val(str);
                    var strname = $("input[name='BillToParty.CompanyName']").val();
                    var lastItem = strname.split(" ").pop();
                    if (isNaN(lastItem)) {
                        $("input[name='BillToParty.CompanyName']").val(strname + ' ' + str)
                    }
                    else {
                        strname = strname.replace(lastItem, str);
                        $("input[name='BillToParty.CompanyName']").val(strname);
                    }
                }
                else {
                    $("input[name='BillToParty.ContactRole']").val("N/A");
                }
            }
            else {
                $("input[name='BillToParty.ContactRole']").val("N/A");
            }
        });


        $(".SaveInvoiceLines").click(function () {
            //HB.TransactionValidationV2.SaveInvoiceLines($("#TaxLine").val());
            HB.TransactionValidationV2.SaveInvoiceLines($("#NewLineIndex").val());
            return false;
        });

        $(".ClearInvoiceLine").click(function () {
            HB.TransactionValidationV2.ClearInvoiceLineData();
            return false;
        });

        $(".SendSupportTicketModal").click(function () {
            HB.TransactionValidationV2.SendSuppotTicket();
            return false;
        });

        $(".CancelSupportTicketModal").click(function () {
            HB.TransactionValidationV2.CancelSupportTicketModal();
            return false;
        });
        $(".SaveDraftCancelCommentModal").click(function () {
            HB.TransactionValidationV2.SaveDraftCancelCommentModal();
            return false;
        });
        $(".SaveDraftSaveCommentModal").click(function () {
            HB.TransactionValidationV2.SaveDraftSaveCommentModal();
            return false;
        });
        $('#IgnoreComments').change(function () {
            if ($(this).is(":checked")) {
                $('#DraftCommentBody').select2('disable');
                $('#DraftCommentBody').summernote('disable');
            }
            else {
                $('#DraftCommentBody').select2('enable');
                $('#DraftCommentBody').summernote('enable');
            }
        });
        $(".toggle-collapse").on("click", function () {
            var strText = $(this).text();
            if (strText == "Collapse All") {
                $(".document-panel-editor .panel-body").css("display", "none");
                $(this).text("Expand All");
                $(".dvcursorpointer").find("i").removeClass("fa fa-chevron-up").addClass("fa fa-chevron-down");
            }
            else {
                $(".document-panel-editor .panel-body").css("display", "block");
                $(this).text("Collapse All");

                $(".dvcursorpointer").find("i").removeClass("fa fa-chevron-down").addClass("fa fa-chevron-up");
            }


        });
        //$("#InvoiceTax").change(function () {
        //    toastr.clear();
        //    RemoveAllError();
        //    var TaxPer = this.value;
        //    var Url = '/TransactionValidationV2/SaveTaxAmount?' + $("#querystring").val();
        //    RM.Ajax.doCallback(Url, {
        //        data: { 'TaxPer': TaxPer, TotalAmount: $("#TotalAmount").val() },
        //        onSuccess: function (PayableAmount, TaxAmount) {
        //            $("#TaxLine").val(TaxPer);
        //            $("#spanTotal").text(PayableAmount);
        //            $("#spanTaxAmount").text(TaxAmount);
        //        },
        //        onError: function (headerData, extraData) {
        //            HB.LoginCommon.StopLoading();
        //            HB.LoginCommon.ErrorMsg(headerData, extraData);
        //        }
        //    });

        //    return false;
        //});

        $("#Quantity,#UnitPrice,#Discount_DiscountPer,#Tax_TaxPer").focusout(function () {
            toastr.clear();
            RemoveAllError();
            var Url = '/TransactionValidationV2/CalculateLineAmount?' + $("#querystring").val();
            RM.Ajax.doCallback(Url, {
                data: { Quantity: $("#Quantity").val(), UnitPrice: $("#UnitPrice").val(), DiscountPer: $("#Discount_DiscountPer").val(), TaxPer: $("#Tax_TaxPer").val() },
                onSuccess: function (data) {
                    $("#NetUnitPrice").tooltip("destroy").removeClass("error").val(data.NetUnitPrice);
                    $("#LineItemAmount").tooltip("destroy").removeClass("error").val(data.LineItemAmount);
                    $("#LineTotalAmount").tooltip("destroy").removeClass("error").val(data.TotalAmount);
                    $("#LineTotalAmountWithTax").tooltip("destroy").removeClass("error").val(data.TotalAmountWithTax);
                    $("#Tax_TaxAmount").tooltip("destroy").removeClass("error").val(data.TaxAmount);
                },
                onError: function (headerData, extraData) {
                    HB.LoginCommon.StopLoading();
                    HB.LoginCommon.ErrorMsg(headerData, extraData);
                }
            });
        });



        $(".SendDocument").click(function () {
            if ($("#IsResubmited").val() == "True") {
                swal({
                    title: 'This file is already sent to the destination, Do you want to still send again?',
                    // text: $("#deletemessage").val(),
                    type: "warning",
                    showCancelButton: true,
                    confirmButtonColor: "#DD6B55",
                    confirmButtonText: $("#btnYes").val(),
                    cancelButtonText: $("#btnNo").val(),
                    closeOnConfirm: true,
                    closeOnCancel: true
                },
            function (isConfirm) {
                if (isConfirm) {
                    var count = 0;
                    $("input[name=Document_Date]").removeClass("alert-danger");
                    $("input[name=Document_No]").removeClass("alert-danger");
                    $("input[name=Currency_Code]").removeClass("alert-danger");
                    $("#Receiver_Endpoint").removeClass("alert-danger");
                    $("#BillToParty_RegNo").removeClass("alert-danger");
                    $("input[name='BillToParty.CompanyName']").removeClass("alert-danger");
                    $("input[name='BillToParty.Address']").removeClass("alert-danger");
                    $("input[name='BillToParty.City']").removeClass("alert-danger");
                    $("input[name='BillToParty.PostCode']").removeClass("alert-danger");
                    $("input[name='BillToParty.Country']").removeClass("alert-danger");
                    $("#ShipToParty_RegNo").removeClass("alert-danger");
                    $("#ShipToParty_CompanyId").removeClass("alert-danger");
                    $("input[name='ShipToParty.CompanyName']").removeClass("alert-danger");
                    $("input[name='ShipToParty.PostCode']").removeClass("alert-danger");
                    $("input[name='ShipToParty.City']").removeClass("alert-danger");
                    $("input[name='ShipToParty.Country']").removeClass("alert-danger");
                    $("input[name='Sender_Endpoint.Value']").removeClass("alert-danger");
                    $("input[name='ShipToParty.PostCode']").removeClass("alert-danger");
                    $("input[name='SupplierParty.RegNo.Value']").removeClass("alert-danger");
                    $("input[name='SupplierParty.ContactName']").removeClass("alert-danger");
                    $("input[name='SupplierParty.CompanyName']").removeClass("alert-danger");
                    $("input[name='SupplierParty.Address']").removeClass("alert-danger");
                    $("input[name='SupplierParty.City']").removeClass("alert-danger");
                    $("input[name='SupplierParty.PostCode']").removeClass("alert-danger");
                    $("input[name='SupplierParty.Country']").removeClass("alert-danger");
                    if ($("input[name=Document_Date]").val() == null || $("input[name=Document_Date]").val() == undefined || $("input[name=Document_Date]").val() == "") {
                        $("input[name=Document_Date]").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name=Document_No]").val() == null || $("input[name=Document_No]").val() == undefined || $("input[name=Document_No]").val() == "") {
                        $("input[name=Document_No]").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name=Currency_Code]").val() == null || $("input[name=Currency_Code]").val() == undefined || $("input[name=Currency_Code]").val() == "") {
                        $("input[name=Currency_Code]").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("#Receiver_Endpoint").val() == null || $("#Receiver_Endpoint").val() == undefined || $("#Receiver_Endpoint").val() == "") {
                        $("#Receiver_Endpoint").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("#BillToParty_RegNo").val() == null || $("#BillToParty_RegNo").val() == undefined || $("#BillToParty_RegNo").val() == "") {
                        $("#BillToParty_RegNo").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='BillToParty.CompanyName']").val() == null || $("input[name='BillToParty.CompanyName']").val() == undefined || $("input[name='BillToParty.CompanyName']").val() == "") {
                        $("input[name='BillToParty.CompanyName']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='BillToParty.Address']").val() == null || $("input[name='BillToParty.Address']").val() == undefined || $("input[name='BillToParty.Address']").val() == "") {
                        $("input[name='BillToParty.Address']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='BillToParty.City']").val() == null || $("input[name='BillToParty.City']").val() == undefined || $("input[name='BillToParty.City']").val() == "") {
                        $("input[name='BillToParty.City']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='BillToParty.PostCode']").val() == null || $("input[name='BillToParty.PostCode']").val() == undefined || $("input[name='BillToParty.PostCode']").val() == "") {
                        $("input[name='BillToParty.PostCode']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='BillToParty.Country']").val() == null || $("input[name='BillToParty.Country']").val() == undefined || $("input[name='BillToParty.Country']").val() == "") {
                        $("input[name='BillToParty.Country']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("#ShipToParty_RegNo").val() == null || $("#ShipToParty_RegNo").val() == undefined || $("#ShipToParty_RegNo").val() == "") {
                        $("#ShipToParty_RegNo").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("#ShipToParty_CompanyId").val() == null || $("#ShipToParty_CompanyId").val() == undefined || $("#ShipToParty_CompanyId").val() == "") {
                        $("#ShipToParty_CompanyId").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='ShipToParty.CompanyName']").val() == null || $("input[name='ShipToParty.CompanyName']").val() == undefined || $("input[name='ShipToParty.CompanyName']").val() == "") {
                        $("input[name='ShipToParty.CompanyName']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='ShipToParty.PostCode']").val() == null || $("input[name='ShipToParty.PostCode']").val() == undefined || $("input[name='ShipToParty.PostCode']").val() == "") {
                        $("input[name='ShipToParty.PostCode']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='ShipToParty.City']").val() == null || $("input[name='ShipToParty.City']").val() == undefined || $("input[name='ShipToParty.City']").val() == "") {
                        $("input[name='ShipToParty.City']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='ShipToParty.Country']").val() == null || $("input[name='ShipToParty.Country']").val() == undefined || $("input[name='ShipToParty.Country']").val() == "") {
                        $("input[name='ShipToParty.Country']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='Sender_Endpoint.Value']").val() == null || $("input[name='Sender_Endpoint.Value']").val() == undefined || $("input[name='Sender_Endpoint.Value']").val() == "") {
                        $("input[name='Sender_Endpoint.Value']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='SupplierParty.RegNo.Value']").val() == null || $("input[name='SupplierParty.RegNo.Value']").val() == undefined || $("input[name='SupplierParty.RegNo.Value']").val() == "") {
                        $("input[name='SupplierParty.RegNo.Value']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='SupplierParty.ContactName']").val() == null || $("input[name='SupplierParty.ContactName']").val() == undefined || $("input[name='SupplierParty.ContactName']").val() == "") {
                        $("input[name='SupplierParty.ContactName']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='SupplierParty.CompanyName']").val() == null || $("input[name='SupplierParty.CompanyName']").val() == undefined || $("input[name='SupplierParty.CompanyName']").val() == "") {
                        $("input[name='SupplierParty.CompanyName']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='SupplierParty.Address']").val() == null || $("input[name='SupplierParty.Address']").val() == undefined || $("input[name='SupplierParty.Address']").val() == "") {
                        $("input[name='SupplierParty.Address']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='SupplierParty.CompanyName']").val() == null || $("input[name='SupplierParty.CompanyName']").val() == undefined || $("input[name='SupplierParty.CompanyName']").val() == "") {
                        $("input[name='SupplierParty.CompanyName']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='SupplierParty.City']").val() == null || $("input[name='SupplierParty.City']").val() == undefined || $("input[name='SupplierParty.City']").val() == "") {
                        $("input[name='SupplierParty.City']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='SupplierParty.PostCode']").val() == null || $("input[name='SupplierParty.PostCode']").val() == undefined || $("input[name='SupplierParty.PostCode']").val() == "") {
                        $("input[name='SupplierParty.PostCode']").addClass("alert-danger");
                        count = 1;
                    }
                    if ($("input[name='SupplierParty.Country']").val() == null || $("input[name='SupplierParty.Country']").val() == undefined || $("input[name='SupplierParty.Country']").val() == "") {
                        $("input[name='SupplierParty.Country']").addClass("alert-danger");
                        count = 1;
                    }

                    if (count == 1) {
                        HB.LoginCommon.ErrorMsg('Please add all mandatory fields');
                    }
                    else {
                        HB.TransactionValidationV2.SendFileToDestination();
                    }

                }
            });
            }
            else {
                var count = 0;
                $("input[name=Document_Date]").removeClass("alert-danger");
                $("input[name=Document_No]").removeClass("alert-danger");
                $("input[name=Currency_Code]").removeClass("alert-danger");
                $("#Receiver_Endpoint").removeClass("alert-danger");
                $("#BillToParty_RegNo").removeClass("alert-danger");
                $("input[name='BillToParty.CompanyName']").removeClass("alert-danger");
                $("input[name='BillToParty.Address']").removeClass("alert-danger");
                $("input[name='BillToParty.City']").removeClass("alert-danger");
                $("input[name='BillToParty.PostCode']").removeClass("alert-danger");
                $("input[name='BillToParty.Country']").removeClass("alert-danger");
                $("#ShipToParty_RegNo").removeClass("alert-danger");
                $("#ShipToParty_CompanyId").removeClass("alert-danger");
                $("input[name='ShipToParty.CompanyName']").removeClass("alert-danger");
                $("input[name='ShipToParty.PostCode']").removeClass("alert-danger");
                $("input[name='ShipToParty.City']").removeClass("alert-danger");
                $("input[name='ShipToParty.Country']").removeClass("alert-danger");
                $("input[name='Sender_Endpoint.Value']").removeClass("alert-danger");
                $("input[name='ShipToParty.PostCode']").removeClass("alert-danger");
                $("input[name='SupplierParty.RegNo.Value']").removeClass("alert-danger");
                $("input[name='SupplierParty.ContactName']").removeClass("alert-danger");
                $("input[name='SupplierParty.CompanyName']").removeClass("alert-danger");
                $("input[name='SupplierParty.Address']").removeClass("alert-danger");
                $("input[name='SupplierParty.City']").removeClass("alert-danger");
                $("input[name='SupplierParty.PostCode']").removeClass("alert-danger");
                $("input[name='SupplierParty.Country']").removeClass("alert-danger");
                if ($("input[name=Document_Date]").val() == null || $("input[name=Document_Date]").val() == undefined || $("input[name=Document_Date]").val() == "") {
                    $("input[name=Document_Date]").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name=Document_No]").val() == null || $("input[name=Document_No]").val() == undefined || $("input[name=Document_No]").val() == "") {
                    $("input[name=Document_No]").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name=Currency_Code]").val() == null || $("input[name=Currency_Code]").val() == undefined || $("input[name=Currency_Code]").val() == "") {
                    $("input[name=Currency_Code]").addClass("alert-danger");
                    count = 1;
                }
                if ($("#Receiver_Endpoint").val() == null || $("#Receiver_Endpoint").val() == undefined || $("#Receiver_Endpoint").val() == "") {
                    $("#Receiver_Endpoint").addClass("alert-danger");
                    count = 1;
                }
                if ($("#BillToParty_RegNo").val() == null || $("#BillToParty_RegNo").val() == undefined || $("#BillToParty_RegNo").val() == "") {
                    $("#BillToParty_RegNo").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='BillToParty.CompanyName']").val() == null || $("input[name='BillToParty.CompanyName']").val() == undefined || $("input[name='BillToParty.CompanyName']").val() == "") {
                    $("input[name='BillToParty.CompanyName']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='BillToParty.Address']").val() == null || $("input[name='BillToParty.Address']").val() == undefined || $("input[name='BillToParty.Address']").val() == "") {
                    $("input[name='BillToParty.Address']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='BillToParty.City']").val() == null || $("input[name='BillToParty.City']").val() == undefined || $("input[name='BillToParty.City']").val() == "") {
                    $("input[name='BillToParty.City']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='BillToParty.PostCode']").val() == null || $("input[name='BillToParty.PostCode']").val() == undefined || $("input[name='BillToParty.PostCode']").val() == "") {
                    $("input[name='BillToParty.PostCode']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='BillToParty.Country']").val() == null || $("input[name='BillToParty.Country']").val() == undefined || $("input[name='BillToParty.Country']").val() == "") {
                    $("input[name='BillToParty.Country']").addClass("alert-danger");
                    count = 1;
                }
                if ($("#ShipToParty_RegNo").val() == null || $("#ShipToParty_RegNo").val() == undefined || $("#ShipToParty_RegNo").val() == "") {
                    $("#ShipToParty_RegNo").addClass("alert-danger");
                    count = 1;
                }
                if ($("#ShipToParty_CompanyId").val() == null || $("#ShipToParty_CompanyId").val() == undefined || $("#ShipToParty_CompanyId").val() == "") {
                    $("#ShipToParty_CompanyId").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='ShipToParty.CompanyName']").val() == null || $("input[name='ShipToParty.CompanyName']").val() == undefined || $("input[name='ShipToParty.CompanyName']").val() == "") {
                    $("input[name='ShipToParty.CompanyName']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='ShipToParty.PostCode']").val() == null || $("input[name='ShipToParty.PostCode']").val() == undefined || $("input[name='ShipToParty.PostCode']").val() == "") {
                    $("input[name='ShipToParty.PostCode']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='ShipToParty.City']").val() == null || $("input[name='ShipToParty.City']").val() == undefined || $("input[name='ShipToParty.City']").val() == "") {
                    $("input[name='ShipToParty.City']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='ShipToParty.Country']").val() == null || $("input[name='ShipToParty.Country']").val() == undefined || $("input[name='ShipToParty.Country']").val() == "") {
                    $("input[name='ShipToParty.Country']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='Sender_Endpoint.Value']").val() == null || $("input[name='Sender_Endpoint.Value']").val() == undefined || $("input[name='Sender_Endpoint.Value']").val() == "") {
                    $("input[name='Sender_Endpoint.Value']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='SupplierParty.RegNo.Value']").val() == null || $("input[name='SupplierParty.RegNo.Value']").val() == undefined || $("input[name='SupplierParty.RegNo.Value']").val() == "") {
                    $("input[name='SupplierParty.RegNo.Value']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='SupplierParty.ContactName']").val() == null || $("input[name='SupplierParty.ContactName']").val() == undefined || $("input[name='SupplierParty.ContactName']").val() == "") {
                    $("input[name='SupplierParty.ContactName']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='SupplierParty.CompanyName']").val() == null || $("input[name='SupplierParty.CompanyName']").val() == undefined || $("input[name='SupplierParty.CompanyName']").val() == "") {
                    $("input[name='SupplierParty.CompanyName']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='SupplierParty.Address']").val() == null || $("input[name='SupplierParty.Address']").val() == undefined || $("input[name='SupplierParty.Address']").val() == "") {
                    $("input[name='SupplierParty.Address']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='SupplierParty.City']").val() == null || $("input[name='SupplierParty.City']").val() == undefined || $("input[name='SupplierParty.City']").val() == "") {
                    $("input[name='SupplierParty.City']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='SupplierParty.PostCode']").val() == null || $("input[name='SupplierParty.PostCode']").val() == undefined || $("input[name='SupplierParty.PostCode']").val() == "") {
                    $("input[name='SupplierParty.PostCode']").addClass("alert-danger");
                    count = 1;
                }
                if ($("input[name='SupplierParty.Country']").val() == null || $("input[name='SupplierParty.Country']").val() == undefined || $("input[name='SupplierParty.Country']").val() == "") {
                    $("input[name='SupplierParty.Country']").addClass("alert-danger");
                    count = 1;
                }

                if (count == 1) {
                    HB.LoginCommon.ErrorMsg('Please add all mandatory fields');
                }
                else {
                    HB.TransactionValidationV2.SendFileToDestination();
                }
                //HB.TransactionValidationV2.SendFileToDestination();
            }
            return false;
        });

        $(document).on("click", ".AddInvoiceLine", function (e) {
            //LineIndex = parseInt($("#TotalLines").val());
            LineIndex = $(this).attr("lineindex");
            if (LineIndex == undefined) {
                LineIndex = parseInt($("#TotalLines").val());
                $("#NewLineIndex").val(Number(LineIndex));
            }
            else {
                $("#NewLineIndex").val(Number(LineIndex) + 1);
            }
            //$("#NewLineIndex").val(Number(LineIndex) + 1);
            LineIndex = null;
            ////LineIndex = $(this).attr("LineIndex");
            IsNewProduct = true;
            HB.TransactionValidationV2.EditInvoiceLines(LineIndex, e);
            return false;
        });

        $(".Validate").click(function () {
            var count = 0;
            $("input[name=Document_Date]").removeClass("alert-danger");
            $("input[name=Document_No]").removeClass("alert-danger");
            $("input[name=Currency_Code]").removeClass("alert-danger");
            $("#Receiver_Endpoint").removeClass("alert-danger");
            $("#BillToParty_RegNo").removeClass("alert-danger");
            $("input[name='BillToParty.CompanyName']").removeClass("alert-danger");
            $("input[name='BillToParty.Address']").removeClass("alert-danger");
            $("input[name='BillToParty.City']").removeClass("alert-danger");
            $("input[name='BillToParty.PostCode']").removeClass("alert-danger");
            $("input[name='BillToParty.Country']").removeClass("alert-danger");
            $("#ShipToParty_RegNo").removeClass("alert-danger");
            $("#ShipToParty_CompanyId").removeClass("alert-danger");
            $("input[name='ShipToParty.CompanyName']").removeClass("alert-danger");
            $("input[name='ShipToParty.PostCode']").removeClass("alert-danger");
            $("input[name='ShipToParty.City']").removeClass("alert-danger");
            $("input[name='ShipToParty.Country']").removeClass("alert-danger");
            $("input[name='Sender_Endpoint.Value']").removeClass("alert-danger");
            $("input[name='ShipToParty.PostCode']").removeClass("alert-danger");
            $("input[name='SupplierParty.RegNo.Value']").removeClass("alert-danger");
            $("input[name='SupplierParty.ContactName']").removeClass("alert-danger");
            $("input[name='SupplierParty.CompanyName']").removeClass("alert-danger");
            $("input[name='SupplierParty.Address']").removeClass("alert-danger");
            $("input[name='SupplierParty.City']").removeClass("alert-danger");
            $("input[name='SupplierParty.PostCode']").removeClass("alert-danger");
            $("input[name='SupplierParty.Country']").removeClass("alert-danger");
            if ($("input[name=Document_Date]").val() == null || $("input[name=Document_Date]").val() == undefined || $("input[name=Document_Date]").val() == "") {
                $("input[name=Document_Date]").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name=Document_No]").val() == null || $("input[name=Document_No]").val() == undefined || $("input[name=Document_No]").val() == "") {
                $("input[name=Document_No]").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name=Currency_Code]").val() == null || $("input[name=Currency_Code]").val() == undefined || $("input[name=Currency_Code]").val() == "") {
                $("input[name=Currency_Code]").addClass("alert-danger");
                count = 1;
            }
            if ($("#Receiver_Endpoint").val() == null || $("#Receiver_Endpoint").val() == undefined || $("#Receiver_Endpoint").val() == "") {
                $("#Receiver_Endpoint").addClass("alert-danger");
                count = 1;
            }
            if ($("#BillToParty_RegNo").val() == null || $("#BillToParty_RegNo").val() == undefined || $("#BillToParty_RegNo").val() == "") {
                $("#BillToParty_RegNo").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='BillToParty.CompanyName']").val() == null || $("input[name='BillToParty.CompanyName']").val() == undefined || $("input[name='BillToParty.CompanyName']").val() == "") {
                $("input[name='BillToParty.CompanyName']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='BillToParty.Address']").val() == null || $("input[name='BillToParty.Address']").val() == undefined || $("input[name='BillToParty.Address']").val() == "") {
                $("input[name='BillToParty.Address']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='BillToParty.City']").val() == null || $("input[name='BillToParty.City']").val() == undefined || $("input[name='BillToParty.City']").val() == "") {
                $("input[name='BillToParty.City']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='BillToParty.PostCode']").val() == null || $("input[name='BillToParty.PostCode']").val() == undefined || $("input[name='BillToParty.PostCode']").val() == "") {
                $("input[name='BillToParty.PostCode']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='BillToParty.Country']").val() == null || $("input[name='BillToParty.Country']").val() == undefined || $("input[name='BillToParty.Country']").val() == "") {
                $("input[name='BillToParty.Country']").addClass("alert-danger");
                count = 1;
            }
            if ($("#ShipToParty_RegNo").val() == null || $("#ShipToParty_RegNo").val() == undefined || $("#ShipToParty_RegNo").val() == "") {
                $("#ShipToParty_RegNo").addClass("alert-danger");
                count = 1;
            }
            if ($("#ShipToParty_CompanyId").val() == null || $("#ShipToParty_CompanyId").val() == undefined || $("#ShipToParty_CompanyId").val() == "") {
                $("#ShipToParty_CompanyId").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='ShipToParty.CompanyName']").val() == null || $("input[name='ShipToParty.CompanyName']").val() == undefined || $("input[name='ShipToParty.CompanyName']").val() == "") {
                $("input[name='ShipToParty.CompanyName']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='ShipToParty.PostCode']").val() == null || $("input[name='ShipToParty.PostCode']").val() == undefined || $("input[name='ShipToParty.PostCode']").val() == "") {
                $("input[name='ShipToParty.PostCode']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='ShipToParty.City']").val() == null || $("input[name='ShipToParty.City']").val() == undefined || $("input[name='ShipToParty.City']").val() == "") {
                $("input[name='ShipToParty.City']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='ShipToParty.Country']").val() == null || $("input[name='ShipToParty.Country']").val() == undefined || $("input[name='ShipToParty.Country']").val() == "") {
                $("input[name='ShipToParty.Country']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='Sender_Endpoint.Value']").val() == null || $("input[name='Sender_Endpoint.Value']").val() == undefined || $("input[name='Sender_Endpoint.Value']").val() == "") {
                $("input[name='Sender_Endpoint.Value']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='SupplierParty.RegNo.Value']").val() == null || $("input[name='SupplierParty.RegNo.Value']").val() == undefined || $("input[name='SupplierParty.RegNo.Value']").val() == "") {
                $("input[name='SupplierParty.RegNo.Value']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='SupplierParty.ContactName']").val() == null || $("input[name='SupplierParty.ContactName']").val() == undefined || $("input[name='SupplierParty.ContactName']").val() == "") {
                $("input[name='SupplierParty.ContactName']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='SupplierParty.CompanyName']").val() == null || $("input[name='SupplierParty.CompanyName']").val() == undefined || $("input[name='SupplierParty.CompanyName']").val() == "") {
                $("input[name='SupplierParty.CompanyName']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='SupplierParty.Address']").val() == null || $("input[name='SupplierParty.Address']").val() == undefined || $("input[name='SupplierParty.Address']").val() == "") {
                $("input[name='SupplierParty.Address']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='SupplierParty.City']").val() == null || $("input[name='SupplierParty.City']").val() == undefined || $("input[name='SupplierParty.City']").val() == "") {
                $("input[name='SupplierParty.City']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='SupplierParty.PostCode']").val() == null || $("input[name='SupplierParty.PostCode']").val() == undefined || $("input[name='SupplierParty.PostCode']").val() == "") {
                $("input[name='SupplierParty.PostCode']").addClass("alert-danger");
                count = 1;
            }
            if ($("input[name='SupplierParty.Country']").val() == null || $("input[name='SupplierParty.Country']").val() == undefined || $("input[name='SupplierParty.Country']").val() == "") {
                $("input[name='SupplierParty.Country']").addClass("alert-danger");
                count = 1;
            }

            if (count == 1) {
                HB.LoginCommon.ErrorMsg('Please add all mandatory fields');
            }
            else {
                HB.TransactionValidationV2.ValidateFile();
            }           
            return false;
        });

        $(".SaveDraft").click(function () {
            $("#SaveDraftCommentModal").modal();
            //HB.TransactionValidationV2.SaveDraft();
            return false;
        });

        $(".XMLEditor").click(function () {
            $("#PageNum").text(2);
            $("#PageNum").val("2");
            HB.TransactionValidationV2.SaveDraft();
            return false;
        });

        $(".SaveReview").click(function () {
            HB.TransactionValidationV2.SaveReview();
            return false;
        });

        HB.TransactionValidationV2.TotalCalculations();

        $("#lstDiscount0DiscountPer").val($("#lstDiscount_0__DiscountPer").text());
        $("#lstCharge0ChargePer").val($("#lstCharge_0__ChargePer").text());
        $("#txtRoundingAmount").val($("#RoundingAmount").text());

        $("#lstDiscount0DiscountPer").change(function () {
            HB.TransactionValidationV2.TotalCalculations();
        });

        $("#lstCharge0ChargePer").change(function () {
            HB.TransactionValidationV2.TotalCalculations();
        });

        $("#txtRoundingAmount").change(function () {
            HB.TransactionValidationV2.TotalCalculations();
        });

        $(".Discard").click(function () {
            HB.TransactionValidationV2.Discard();
            return false;
        });
        HB.TransactionValidationV2.AddEditDeleteEvent();
        $(".invoiceLineModel-dialog").mousedown(function () {
            $(".invoiceLineModel-content").addClass("invoiceLineModel-content-shadow");
        });
        $(".invoiceLineModel-dialog").mouseup(function () {
            $(".invoiceLineModel-content").removeClass("invoiceLineModel-content-shadow");
        });

        $("#btnGetAIData").click(function () {
            HB.TransactionValidationV2.GetAIData();
        });
    }

    this.AddEditDeleteEvent = function () {
        $(".EditInvoiceLine").click(function (e) {
            $("#YPos").val($(this).offset().top);
            LineIndex = $(this).attr("LineIndex");
            $("#NewLineIndex").val(Number(LineIndex));
            IsNewProduct = false;
            HB.TransactionValidationV2.EditInvoiceLines(LineIndex, e)
            return false;
        });

        $(".DeleteInvoiceLine").click(function () {
            HB.TransactionValidationV2.InvoiceLineDelete($(this).attr("LineIndex"));
            return false;
        });
    }

    this.ApplyXEditableToField = function () {
        //TO DO NAYAN: apply method to check validations
        //$('.editable').editable({
        //    url: '/TransactionValidationV2/CheckValidation?' + $("#querystring").val(),
        //    type: 'text',
        //    pk: 1,
        //    savenochange: true,
        //    //  emptytext:'blank',
        //    success: function (data) {
        //        if (data.success) {
        //            var Ele = document.getElementsByName(data.message);
        //            Ele[0].classList.remove("editable-error");
        //        }
        //        else {
        //            return data.extraData;
        //        }
        //    },
        //});

        HB.TransactionValidationV2.AddEditDeleteEvent();

    }

    this.ApplyXEditableToParty = function (id, Party) {
        //TO DO NAYAN: apply method to check validations for endpointid
        //$('#' + id).editable({
        //    url: '/TransactionValidationV2/CheckValidationEndpointId?' + $("#querystring").val(),
        //    type: 'post',
        //    pk: 1,
        //    savenochange: true,
        //    value: {
        //        Qualifier: Party.Qualifier,
        //        Value: Party.Value,
        //    },
        //    success: function (data) {
        //        if (data.success) {
        //            Party = data.redirectURL;
        //            var Ele = document.getElementsByName(data.message);
        //            Ele[0].classList.remove("editable-error");
        //        }
        //        else {
        //            return data.extraData;
        //        }
        //    },
        //});
    }

    //extra method
    this.ApplyXEditableToParty2 = function (id, Party) {
        $("#" + id + "_Value").editable({
            url: '/TransactionValidationV2/CheckValidationEndpointId?' + $("#querystring").val(),
            type: 'post',
            pk: 1,
            savenochange: true,
            value: {
                Qualifier: Party.Qualifier,
                Value: Party.Value,
            },
            success: function (data) {
                if (data.success) {
                    Party = data.redirectURL;
                    var Ele = document.getElementsByName(data.message);
                    Ele[0].classList.remove("editable-error");
                }
                else {
                    return data.extraData;
                }
            },
        });
    }
    this.Set_Qualifier = function (id) {
        var data = HB.TransactionValidationV2.GetQualifierList();
        $('#' + id + "_Qualifier").editable({
            type: 'select',
            pk: 1,
            emptytext: 'Empty',
            savenochange: true,
            source: data
        });
    }
    this.GetQualifierList = function () {
        QualifierList = [];
        $.getJSON('/TransactionValidationV2/GetQualifierList?', function (data) {
            $.each(data, function (index) {
                item = {}
                item["value"] = data[index].Value;
                item["text"] = data[index].Text;
                QualifierList.push(item);
            });
        });
        return QualifierList;
    }

    this.GetCountryList = function () {
        CountryList = [];
        $.getJSON('/TransactionValidationV2/GetCountryList?', function (data) {
            $.each(data, function (index) {
                item = {}
                item["value"] = data[index].Value;
                item["text"] = data[index].Text;
                CountryList.push(item);
            });
        });
        return CountryList;
    }

    this.SetCountryList = function (id) {
        var data = HB.TransactionValidationV2.GetCountryList();
        $('#' + id).editable({
            type: 'select',
            pk: 1,
            emptytext: 'Empty',
            savenochange: true,
            source: data,
        });


        //var jsonstring = '';
        //$.getJSON('/TransactionValidationV2/GetCountryList?', function (data) {
        //    jsonstring += "[";
        //    $.each(data, function (key, value) {
        //        if (data.length != key)
        //            jsonstring += "{value: '" + value.Value + "', text: '" + value.Text + "'},";
        //        else
        //            jsonstring += "{value: '" + value.Value + "', text: '" + value.Text + "'}";
        //    });
        //    jsonstring.append += "]";

        //    alert(jsonstring);
        //});
        //$('#' + id).editable({
        //    type: 'select',
        //    url:'/post',
        //    pk: 1,            
        //    emptytext: 'empty',
        //    width: '230px',
        //    source: jsonstring,
        //    sourceCache:true
        //});

        //var country_codes = [];
        //country_codes=  $.getJSON('/TransactionValidationV2/GetCountryList?', function (data) {
        //    $.each(data, function (index) {
        //        country_codes.push({
        //            id: data[index].Value,
        //            text: data[index].Text
        //        });
        //    });
        //});
        //alert(JSON.stringify(country_codes));


        //Use this code if want to apply select2
        //$('#' + id).editable({
        //    type: 'select2',
        //    //url:'/post',
        //    pk: 1,
        //    onblur: 'submit',
        //    emptytext: 'Empty',
        //    savenochange: true,
        //    select2: {
        //        placeholder: 'Select Country',
        //        //allowClear: true,
        //        width: '230px',
        //        //minimumInputLength: 2,
        //        id: function (e) {
        //            return e.Value;
        //        },
        //        ajax: {
        //            url: '/TransactionValidationV2/GetCountryList?' + $("#querystring").val(),
        //            dataType: 'json',
        //            data: function (term, page) {
        //                return { query: term };
        //            },
        //            results: function (data, page) {
        //                return { results: data };
        //            },
        //        },
        //        formatResult: function (Country) {
        //            return Country.Text;
        //        },
        //        formatSelection: function (Country) {
        //            return Country.Value;
        //        },
        //        initSelection: function (element, callback) {
        //            return $.get('/TransactionValidationV2/GetCountryByCode', { query: element.val() }, function (data) {
        //                callback(data);
        //            }, 'json'); //added dataType
        //        }
        //    },
        //});
    }


    this.SendFileToDestination = function () {
        if (RM.FormValidation.ValidateId("TransactionValidationForm", "formvalidationmsg")) {
            var Url = '/TransactionValidationV2/SendFileToDestination?' + $("#querystring").val();
            HB.LoginCommon.StartLoading();
            RM.Ajax.doCallback(Url, {
                data: $.param($('.TranValidation').map(function () {
                    return { name: this.name, value: ((this.value == "" || this.value == undefined) ? (this.text == "" ? "" : this.text) : this.value) };
                })),
                onSuccess: function (extraData, redirectURL) {
                    HB.LoginCommon.StopLoading();
                    $("#IsResubmited").val("True");
                    HB.LoginCommon.SuccessMsg(extraData, redirectURL);
                },
                onError: function (headerData, ShowMsgInPopup, Messages) {
                    HB.LoginCommon.StopLoading();
                    if (ShowMsgInPopup == 1) {
                        HB.LoginCommon.ErrorMsg(headerData);
                    }
                    else if (ShowMsgInPopup == 2) {
                        $('.TranValidation').each(function () {
                            var element = $(this);
                            $(headerData).each(function (index) {
                                if ($(headerData)[index].Item4 == 0) {
                                    if ((typeof element.attr("extraData") !== 'undefined') && element.attr("extraData") == $(headerData)[index].Item1) {
                                        $(element).addClass("alert-danger");
                                    }
                                }
                                else if ((typeof element.attr("extraData") !== 'undefined')) {
                                    if (element.attr("extraData") == $(headerData)[index].Item1 + "_" + $(headerData)[index].Item4)
                                        $(element).addClass("alert-danger");

                                    //$(headerData)[index].Item1 + "_" + $(headerData)[index].Item4
                                    //element.attr("extraData") + "_" + $(headerData)[index].Item4
                                }

                            });
                        })
                        if (Messages != '') {
                            //HB.LoginCommon.ErrorMsg(Messages);
                            $("#ValidationErrorModal").modal();
                            $("#dvValidationErrors").empty();
                            $("#dvValidationErrors").html(Messages);
                            HB.TransactionValidationV2.HighlightErrors(Messages);
                        }
                    }
                    else {
                        swal({
                            title: headerData,
                            // text: $("#deletemessage").val(),
                            type: "warning",
                            showCancelButton: true,
                            confirmButtonColor: "#DD6B55",
                            confirmButtonText: "Ok",
                            cancelButtonText: "Cancel",
                            closeOnConfirm: true,
                            closeOnCancel: true
                        },
                        function (isConfirm) {
                            if (isConfirm) {
                                HB.TransactionValidationV2.SendSuppotTicketModal();
                            }
                            else {
                                //window.location.href = '/DashBoard';
                                //return false;
                            }
                        });
                    }
                }
            });
        }
        return false;
    };

    this.EditInvoiceLines = function (LineIndex, event) {
        HB.TransactionValidationV2.SetModalValue("Line_No", "lstLines_Line_No_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("Customer_Line_Reference_No", "lstCustomer_Line_Reference_No_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("Supplier_ItemNo", "lstLines_Supplier_ItemNo_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("EANNo", "lstLines_EANNo_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("Description", "lstLines_Description_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("Description2", "lstLines_Description2_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("Customer_ItemNo", "lstLines_Customer_ItemNo_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("InternalUnitOfMeasure", "lstLines_InternalUnitOfMeasure_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("UnitOfMeasure", "lstLines_UnitOfMeasure_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("Quantity", "lstLines_Quantity_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("ExternalQuantity", "lstLines_ExternalQuantity_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("UnitPrice", "lstLines_UnitPrice_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("Tax_TaxPer", "lstLines_Tax_TaxPer_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("Tax_TaxAmount", "lstLines_Tax_TaxAmount_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("Discount_DiscountPer", "lstLines_Discount_DiscountPer_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("NetUnitPrice", "lstLines_NetUnitPrice_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("LineItemAmount", "lstLines_LineItemAmount_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("LineTotalAmount", "lstLines_TotalAmount_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("LineTotalAmountWithTax", "lstLines_TotalAmountWithTax_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("DeliveryDate", "lstLines_DeliveryDate_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("Notes", "lstLines_Notes_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("labelInformation", "lstLines_labelInformation_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("labelInformation2", "lstLines_labelInformation2_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("labelInformation3", "lstLines_labelInformation3_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("MinimumQuantity", "lstLines_MinimumQuantity_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("UnitCost", "lstLines_UnitCost_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("RetailPrice", "lstLines_RetailPrice_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("StartDate", "lstLines_StartDate_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("EndDate", "lstLines_EndDate_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("StyleNo", "lstLines_StyleNo_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("BrandCode", "lstLines_BrandCode_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("BrandName", "lstLines_BrandName_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("SeasonCode", "lstLines_SeasonCode_", LineIndex);
        HB.TransactionValidationV2.SetModalValue("SupplierArticleGroup", "lstLines_SupplierArticleGroup_", LineIndex);

        HB.TransactionValidationV2.SetDefaultValue("lstLines_Tax_TaxAmount_", LineIndex, 0, "Tax_TaxAmount");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_TotalAmount_", LineIndex, 0, "LineTotalAmount");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_TotalAmountWithTax_", LineIndex, 0, "LineTotalAmountWithTax");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_LineItemAmount_", LineIndex, 0, "LineItemAmount");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_NetUnitPrice_", LineIndex, 0, "NetUnitPrice");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_Discount_DiscountPer_", LineIndex, 0, "Discount_DiscountPer");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_Tax_TaxPer_", LineIndex, 0, "Tax_TaxPer");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_UnitPrice_", LineIndex, 0, "UnitPrice");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_Quantity_", LineIndex, 0, "Quantity");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_ExternalQuantity_", LineIndex, 0, "ExternalQuantity");
        if ($("#hdnDocFormat").val() == "UBL") {
            HB.TransactionValidationV2.SetDefaultValue("lstLines_ExternalQuantity_", LineIndex, 1, "ExternalQuantity");
        }
        HB.TransactionValidationV2.SetDefaultValue("lstLines_Line_No_", LineIndex, '', "Line_No");
        HB.TransactionValidationV2.SetDefaultValue("lstCustomer_Line_Reference_No_", LineIndex, '', "Customer_Line_Reference_No");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_Description_", LineIndex, '', "Description");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_Description2_", LineIndex, '', "Description2");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_Notes_", LineIndex, '', "Notes");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_labelInformation_", LineIndex, '', "labelInformation");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_labelInformation2_", LineIndex, '', "labelInformation2");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_labelInformation3_", LineIndex, '', "labelInformation3");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_EANNo_", LineIndex, '', "EANNo");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_Customer_ItemNo_", LineIndex, '', "Customer_ItemNo");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_Supplier_ItemNo_", LineIndex, '', "Supplier_ItemNo");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_InternalUnitOfMeasure_", LineIndex, '', "InternalUnitOfMeasure");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_UnitOfMeasure_", LineIndex, 'EA', "UnitOfMeasure");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_DeliveryDate_", LineIndex, '', "DeliveryDate");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_StartDate_", LineIndex, '', "StartDate");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_EndDate_", LineIndex, '', "EndDate");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_MinimumQuantity_", LineIndex, 0, "MinimumQuantity");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_UnitCost_", LineIndex, 0, "UnitCost");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_RetailPrice_", LineIndex, 0, "RetailPrice");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_StyleNo_", LineIndex, '', "StyleNo");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_BrandCode_", LineIndex, '', "BrandCode");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_BrandName_", LineIndex, '', "BrandName");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_SeasonCode_", LineIndex, '', "SeasonCode");
        HB.TransactionValidationV2.SetDefaultValue("lstLines_SupplierArticleGroup_", LineIndex, '', "SupplierArticleGroup");

        $("#invoiceLineModel").removeClass("dvhide");
        $("#invoiceLineModel").css("position", "absolute");
        $("#invoiceLineModel").css("left", "3%");
        $("#invoiceLineModel").css("top", $(window).scrollTop() - 100);        // "77%");
        $('.invoiceLineModel-dialog').draggable({
            handle: ".invoiceLineModel-header"
        });
        $('.invoiceLineModel-dialog').css("margin", 0);
        //$("#" + id);
    }

    this.SetModalValue = function (id, ValueId, LineIndex) {
        $("#" + id).tooltip("destroy").removeClass("error").val($("#" + ValueId + LineIndex).text());
    }

    this.SetDefaultValue = function (id, index, defaultValue, setid) {
        if ($("#" + id + index).text() == '' || $("#" + id + index).text() == 'null' || $("#" + id + index).text() == 'Empty')
            $("#" + setid).val(defaultValue);
    }

    this.InvoiceLineDelete = function (LineIndex) {
        swal({
            title: $("#deleteInvoicelineheader").val(),
            // text: $("#deletemessage").val(),
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: $("#deletebtnOk").val(),
            cancelButtonText: $("#deletebtnCancel").val(),
            closeOnConfirm: true,
            closeOnCancel: true
        },
        function (isConfirm) {
            if (isConfirm) {
                $("#lstLines_Deleted_" + LineIndex).text(true);
                $("#lstLines_Inserted_" + LineIndex).text(false);
                $("#Row_" + LineIndex).addClass("dvhide");
                HB.TransactionValidationV2.TotalCalculations();
            }
        });
        return false;
    }

    this.ApplyEmptyClass = function (id, value) {
        if (value == '' || value == 'null' || value == 'Empty')
            $("#" + id + LineIndex).addClass("editable-empty");
        else
            $("#" + id + LineIndex).text(value);
    }

    this.SaveInvoiceLines = function (TaxValue) {
        RemoveAllError();
        var count = 0;
        $("input[name=Line_No]").removeClass("alert-danger");
        $("input[name=Quantity]").removeClass("alert-danger");
        $("input[name=UnitPrice]").removeClass("alert-danger");
        $("textarea[name=Description]").removeClass("alert-danger");
        toastr.options.closeButton = true;
        if ($("input[name=Line_No]").val() == null || $("input[name=Line_No]").val() == undefined || $("input[name=Line_No]").val() == "") {
            $("input[name=Line_No]").addClass("alert-danger");
            //toastr.error('please enter line no');
            count = 1;
        }
        if ($("input[name=Quantity]").val() == null || $("input[name=Quantity]").val() == undefined || $("input[name=Quantity]").val() == "0" || $("input[name=Quantity]").val() == "") {
            $("input[name=Quantity]").addClass("alert-danger");
            //toastr.error('please enter quantity');
            count = 1;
        }
        if ($("input[name=UnitPrice]").val() == null || $("input[name=UnitPrice]").val() == undefined || $("input[name=UnitPrice]").val() == "0" || $("input[name=UnitPrice]").val() == "") {
            $("input[name=UnitPrice]").addClass("alert-danger");
            //toastr.error('please enter unitprice');
            count = 1;
        }
        if ($("textarea[name=Description]").val() == null || $("textarea[name=Description]").val() == undefined || $("textarea[name=Description]").val() == "") {
            $("textarea[name=Description]").addClass("alert-danger");
            //toastr.error('please enter description');
            count = 1;
        }
        if (count == 1) {
            toastr.error('Please add all mandatory fields');
        }
        else if (RM.FormValidation.ValidateId("InvoiceLinesForm", "formvalidationmsg")) {     //(hide for datemodelbinder)
           $("#TaxPer").val($("#TaxLine").val());
           var LineIndex = Number($("#NewLineIndex").val());
           var Url = '/TransactionValidationV2/SaveInvoiceLines?' + $("#querystring").val();
           HB.LoginCommon.StartLoading();
           RM.Ajax.doCallback(Url, {
               stateContainerId: 'InvoiceLinesContainer',
               onSuccess: function (model) {
                   var EnumIndex = parseInt(LineIndex) + 1;
                   var html = '';
                   if (IsNewProduct) {
                       $("#TotalLines").val(Number($("#TotalLines").val()) + 1);
                       html += '<tr id="Row_' + LineIndex + '">';
                       if (model.Master_Line_No == null || model.Master_Line_No == "") {
                           model.Master_Line_No = EnumIndex;
                       }
                   }
                   html += '<td>';
                   html += '<div class="dvhide">';
                   html += '<a class="TranValidation" id="lstLines_Deleted_' + LineIndex + '" name="lstLines[' + LineIndex + '].Deleted">False</a>';
                   html += '<a class="TranValidation" id="lstLines_Inserted_' + LineIndex + '" name="lstLines[' + LineIndex + '].Inserted">True</a>';
                   html += '<a class="TranValidation" id="lstLines_LineItemAmount_' + LineIndex + '" name="lstLines[' + LineIndex + '].LineItemAmount">' + model.LineItemAmount + '</a>';
                   html += '<a class="TranValidation" id="lstLines_TotalAmountWithTax_' + LineIndex + '" name="lstLines[' + LineIndex + '].TotalAmountWithTax">' + model.TotalAmountWithTax + '</a>';
                   html += '<a class="TranValidation" id="lstLines_Tax_TaxAmount_' + LineIndex + '" name="lstLines[' + LineIndex + '].Tax.TaxAmount">' + model.Tax.TaxAmount + '</a>';
                   html += '<a class="TranValidation" id="lstLines_Tax_TaxableAmount_' + LineIndex + '" name="lstLines[' + LineIndex + '].Tax.TaxableAmount">' + model.Tax.TaxableAmount + '</a>';
                   html += '<a class="TranValidation" id="lstLines_Tax_Reason_' + LineIndex + '" name="lstLines[' + LineIndex + '].Tax.Reason">' + model.Tax.Reason + '</a>';
                   html += '<a class="TranValidation" id="lstLines_Discount_DiscountAmount_' + LineIndex + '" name="lstLines[' + LineIndex + '].Discount.DiscountAmount">' + model.Discount.DiscountAmount + '</a>';
                   html += '<a class="TranValidation" id="lstLines_Discount_DiscountBaseAmount_' + LineIndex + '" name="lstLines[' + LineIndex + '].Discount.DiscountBaseAmount">' + model.Discount.DiscountBaseAmount + '</a>';
                   html += '<a class="TranValidation" id="lstLines_Master_Line_No_' + LineIndex + '" name="lstLines[' + LineIndex + '].Master_Line_No">' + model.Master_Line_No + '</a>';
                   html += '</div>';
                   html += '<div class="input-group btn-group-vertical">';
                   html += '<a class="btn btn-primary btn-xs AddInvoiceLine" lineindex="' + LineIndex + '">';
                   html += '<i class="fa fa-plus"></i>';
                   html += '</a>';
                   html += '<a class="btn btn-warning btn-xs EditInvoiceLine" lineindex="' + LineIndex + '">';
                   html += '<i class="fa fa-edit"></i>';
                   html += '</a>';
                   html += '<a class="btn btn-danger btn-xs DeleteInvoiceLine" lineindex="' + LineIndex + '">';
                   html += '<i class="fa fa-trash"></i>';
                   html += '</a>';
                   html += '</div>';
                   html += ' </td>';
                   html += '<td><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_Line_No_' + LineIndex + '" extradata="' + $("#Enum_Line_No").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].Line_No">' + model.Line_No + '</a></td>';
                   if ($("#hdnDocFormat").val() == "UBL") {
                       html += '<td><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstCustomer_Line_Reference_No_' + LineIndex + '" extradata="' + $("#Enum_Customer_Line_Reference_No").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].Customer_Line_Reference_No">' + model.Customer_Line_Reference_No + '</a></td>';
                   }
                   html += '<td class="wordbreak">';
                   html += '<div><strong><a class="TranValidation EditInvoiceLine " LineIndex="' + LineIndex + '" id="lstLines_Description_' + LineIndex + '" extradata="' + $("#Enum_Line_Description").val() + "_" + EnumIndex + '" data-type="wysihtml5" name="lstLines[' + LineIndex + '].Description">' + model.Description + '</a></strong></div>';
                   if ($("#hdnDocFormat").val() != "FINVOICE") {
                       html += '<small><a class="TranValidation EditInvoiceLine " LineIndex="' + LineIndex + '" id="lstLines_Description2_' + LineIndex + '" extradata="' + $("#Enum_Line_Description2").val() + "_" + EnumIndex + '" data-type="wysihtml5" name="lstLines[' + LineIndex + '].Description2">' + model.Description2 + '</a></small><br>';
                   }
                   if ($("#hdnDocFormat").val() != "CXML") {
                       html += '<small><b>' + $("#lbl_EANNo").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_EANNo_' + LineIndex + '"  name="lstLines[' + LineIndex + '].EANNo">' + model.EANNo + '</a> </small><br>';
                   }
                   html += '<small><b>' + $("#lbl_CustomerItemNo").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_Customer_ItemNo_' + LineIndex + '" extradata="' + $("#Enum_Line_Customer_ItemNo").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].Customer_ItemNo">' + model.Customer_ItemNo + '</a> </small><br>';
                   html += '<small><b>' + $("#lbl_SupplierItemNo").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_Supplier_ItemNo_' + LineIndex + '" extradata="' + $("#Enum_Line_Supplier_ItemNo").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].Supplier_ItemNo">' + model.Supplier_ItemNo + '</a> </small><br>';
                   html += '<small><b>' + $("#lbl_Note").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_Notes_' + LineIndex + '" extradata="' + $("#Enum_Line_Notes").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].Notes">' + model.Notes + '</a> </small><br />';
                   if ($("#hdnDocFormat").val() == "CXML" && $("#hdnDocType").val() == "Order") {
                       html += '<small><b>' + $("#lbl_labelInformation").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_labelInformation_' + LineIndex + '" extradata="' + $("#Enum_Line_labelInformation").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].labelInformation">' + model.labelInformation + '</a> </small><br />';
                       html += '<small><b>' + $("#lbl_labelInformation2").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_labelInformation2_' + LineIndex + '" extradata="' + $("#Enum_Line_labelInformation2").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].labelInformation2">' + model.labelInformation2 + '</a> </small><br />';
                       html += '<small><b>' + $("#lbl_labelInformation3").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_labelInformation3_' + LineIndex + '" extradata="' + $("#Enum_Line_labelInformation3").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].labelInformation3">' + model.labelInformation3 + '</a> </small><br />';
                   }
                   if ($("#hdnDocType").val() == "Order" && $("#hdnDocFormat").val() == "OIOUBL") {
                       html += '<small><b>' + $("#lbl_Line_DeliveryDate").val() + ': </b><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_DeliveryDate_' + LineIndex + '" extradata="' + $("#Enum_Line_DeliveryDate").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].DeliveryDate" data-type="combodate" data-value="' + model.DeliveryDateString + '" data-format="DD-MMM-YYYY" data-viewformat="DD/MM/YYYY" data-placement="left" data-template="DD / MMM / YYYY"></a></small><br>';
                   }
                   if ($("#hdnDocType").val() == "Catalogue") {
                       html += '<small><b>Style No: </b><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_StyleNo' + LineIndex + '" name="lstLines[' + LineIndex + '].StyleNo">' + model.StyleNo + '</a> </small><br />';
                       html += '<small><b>Brand Code: </b><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_BrandCode_' + LineIndex + '" name="lstLines[' + LineIndex + '].BrandCode">' + model.BrandCode + '</a> &nbsp;&nbsp;</small><br />';
                       html += '<small><b>Brand Name: </b><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_BrandName_' + LineIndex + '" name="lstLines[' + LineIndex + '].BrandName">' + model.BrandName + '</a> </small><br />';
                       html += '<small><b>Season Code: </b><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_SeasonCode_' + LineIndex + '" name="lstLines[' + LineIndex + '].SeasonCode">' + model.SeasonCode + '</a> </small><br />';
                       html += '<small><b>Supplier Article Group: </b><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_SupplierArticleGroup_' + LineIndex + '" name="lstLines[' + LineIndex + '].SupplierArticleGroup">' + model.SupplierArticleGroup + '</a> </small><br />';
                   }
                   html += '</td>';
                   if ($("#hdnDocType").val() == "Catalogue") {
                       html += '<td class="wordbreak"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_StartDate_' + LineIndex + '" name="lstLines[' + LineIndex + '].StartDate" data-type="combodate" data-value="' + model.StartDateString + '" data-format="DD-MMM-YYYY" data-viewformat="DD/MM/YYYY" data-placement="left" data-template="DD / MMM / YYYY" data-pk="1"></a></td>';
                       html += '<td class="wordbreak"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_EndDate_' + LineIndex + '" name="lstLines[' + LineIndex + '].EndDate" data-type="combodate" data-value="' + model.EndDateString + '" data-format="DD-MMM-YYYY" data-viewformat="DD/MM/YYYY" data-placement="left" data-template="DD / MMM / YYYY" data-pk="1"></a></td>';
                       html += '<td class="text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_MinimumQuantity_' + LineIndex + '" name="lstLines[' + LineIndex + '].MinimumQuantity">' + model.MinimumQuantity + '</a></td>';
                       html += '<td class="wordbreak text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_UnitOfMeasure_' + LineIndex + '" extradata="' + $("#Enum_Line_UnitOfMeasure").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].UnitOfMeasure">' + model.UnitOfMeasure + '</a></td>';
                       html += '<td class="text-right"><a class="TranValidation  EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_UnitCost_' + LineIndex + '" name="lstLines[' + LineIndex + '].UnitCost">' + model.UnitCost + '</a></td>';
                       html += '<td class="text-right"><a class="TranValidation EditInvoiceLine"  lineindex="' + LineIndex + '" id="lstLines_UnitPrice_' + LineIndex + '" name="lstLines[' + LineIndex + '].UnitPrice">' + model.UnitPrice + '</a></td>';
                       html += '<td class="text-right"><a class="TranValidation" id="lstLines_RetailPrice_' + LineIndex + '" name="lstLines[' + LineIndex + '].RetailPrice">' + model.RetailPrice + '</a></td>';
                   }
                   else {
                       html += '<td class="text-right"><a class="TranValidation EditInvoiceLine"  lineindex="' + LineIndex + '" id="lstLines_Quantity_' + LineIndex + '" name="lstLines[' + LineIndex + '].Quantity">' + model.Quantity + '</a></td>';
                       html += '<td class="text-right"><a class="TranValidation EditInvoiceLine"  lineindex="' + LineIndex + '" id="lstLines_UnitPrice_' + LineIndex + '" name="lstLines[' + LineIndex + '].UnitPrice">' + model.UnitPrice + '</a></td>';
                       if ($("#hdnDocFormat").val() == "CXML") {
                           html += '<td class="wordbreak text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_InternalUnitOfMeasure_' + LineIndex + '" extradata="' + $("#Enum_Line_InternalUnitOfMeasure").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].InternalUnitOfMeasure">' + model.InternalUnitOfMeasure + '</a></td>';
                           html += '<td class="wordbreak text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_UnitOfMeasure_' + LineIndex + '" extradata="' + $("#Enum_Line_UnitOfMeasure").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].UnitOfMeasure">' + model.UnitOfMeasure + '</a></td>';
                           html += '<td class="text-right"><a class="TranValidation EditInvoiceLine"  lineindex="' + LineIndex + '" id="lstLines_ExternalQuantity_' + LineIndex + '" extradata="' + $("#Enum_Line_ExternalQuantity").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].ExternalQuantity">' + model.ExternalQuantity + '</a></td>';
                           html += '<td class="wordbreak"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_DeliveryDate_' + LineIndex + '" extradata="' + $("#Enum_Line_DeliveryDate").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].DeliveryDate" data-type="combodate" data-value="' + model.DeliveryDateString + '" data-format="DD-MMM-YYYY" data-viewformat="DD/MM/YYYY" data-placement="left" data-template="DD / MMM / YYYY"></a></td>';
                       }
                       else if ($("#hdnDocFormat").val() == "UBL") {
                           html += '<td class="text-right"><a class="TranValidation EditInvoiceLine"  lineindex="' + LineIndex + '" id="lstLines_ExternalQuantity_' + LineIndex + '" extradata="' + $("#Enum_Line_ExternalQuantity").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].ExternalQuantity">' + model.ExternalQuantity + '</a></td>';
                           html += '<td class="wordbreak text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_UnitOfMeasure_' + LineIndex + '" extradata="' + $("#Enum_Line_UnitOfMeasure").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].UnitOfMeasure">' + model.UnitOfMeasure + '</a></td>';
                           html += '<td class="text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_Discount_DiscountPer_' + LineIndex + '" name="lstLines[' + LineIndex + '].Discount.DiscountPer">' + model.Discount.DiscountPer + '</a></td>';
                           html += '<td class="wordbreak"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_DeliveryDate_' + LineIndex + '" extradata="' + $("#Enum_Line_DeliveryDate").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].DeliveryDate" data-type="combodate" data-value="' + model.DeliveryDateString + '" data-format="DD-MMM-YYYY" data-viewformat="DD/MM/YYYY" data-placement="left" data-template="DD / MMM / YYYY"></a></td>';
                           html += '<td class="text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_NetUnitPrice_' + LineIndex + '" name="lstLines[' + LineIndex + '].NetUnitPrice">' + model.NetUnitPrice + '</a></td>';
                       }
                       else {
                           html += '<td class="wordbreak text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + LineIndex + '" id="lstLines_UnitOfMeasure_' + LineIndex + '" extradata="' + $("#Enum_Line_UnitOfMeasure").val() + "_" + EnumIndex + '" name="lstLines[' + LineIndex + '].UnitOfMeasure">' + model.UnitOfMeasure + '</a></td>';
                           html += '<td class="text-right"><a class="TranValidation" id="lstLines_Discount_DiscountPer_' + LineIndex + '" name="lstLines[' + LineIndex + '].Discount.DiscountPer">' + model.Discount.DiscountPer + '</a></td>';
                           html += '<td class="text-right"><a class="TranValidation" id="lstLines_Tax_TaxPer_' + LineIndex + '" name="lstLines[' + LineIndex + '].Tax.TaxPer">' + model.Tax.TaxPer + '</a></td>';
                           html += '<td class="text-right"><a class="TranValidation" id="lstLines_NetUnitPrice_' + LineIndex + '" name="lstLines[' + LineIndex + '].NetUnitPrice">' + model.NetUnitPrice + '</a></td>';
                       }
                       html += '<td class="text-right"><a class="TranValidation" id="lstLines_TotalAmount_' + LineIndex + '" name="lstLines[' + LineIndex + '].TotalAmount">' + model.TotalAmount + '</a></td>';
                   }
                   if (IsNewProduct)
                       html += '</tr>';
                   if (IsNewProduct) {
                       //$("#TotalLines").val(LineIndex + 1);
                       if (LineIndex >= $("#InvoiceLineTable tbody tr").length) {
                           $("#InvoiceLineTable tbody").append(html);
                       }
                       else {
                           $("#InvoiceLineTable tbody tr").each(function(item, row) {
                               if(item >= LineIndex) {
                                   $(this).attr("id", "Row_" + (item + 1));

                                   var htmledt = '';
                                   htmledt += '<td>';
                                   htmledt += '<div class="dvhide">';
                                   htmledt += '<a class="TranValidation" id="lstLines_Deleted_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Deleted">' + $(this).find("#lstLines_Deleted_" + (item) + "").text() + '</a>';
                                   htmledt += '<a class="TranValidation" id="lstLines_Inserted_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Inserted">' + $(this).find("#lstLines_Inserted_" + (item) + "").text() + '</a>';
                                   htmledt += '<a class="TranValidation" id="lstLines_LineItemAmount_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].LineItemAmount">' + $(this).find("#lstLines_LineItemAmount_" + (item) + "").text() + '</a>';
                                   htmledt += '<a class="TranValidation" id="lstLines_TotalAmountWithTax_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].TotalAmountWithTax">' + $(this).find("#lstLines_TotalAmountWithTax_" + (item) + "").text() + '</a>';
                                   htmledt += '<a class="TranValidation" id="lstLines_Tax_TaxAmount_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Tax.TaxAmount">' + $(this).find("#lstLines_Tax_TaxAmount_" + (item) + "").text() + '</a>';
                                   htmledt += '<a class="TranValidation" id="lstLines_Tax_TaxableAmount_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Tax.TaxableAmount">' + $(this).find("#lstLines_Tax_TaxableAmount_" + (item) + "").text() + '</a>';
                                   htmledt += '<a class="TranValidation" id="lstLines_Tax_Reason_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Tax.Reason">' + $(this).find("#lstLines_Tax_Reason_" + (item) + "").text() + '</a>';
                                   htmledt += '<a class="TranValidation" id="lstLines_Discount_DiscountAmount_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Discount.DiscountAmount">' + $(this).find("#lstLines_Discount_DiscountAmount_" + (item) + "").text() + '</a>';
                                   htmledt += '<a class="TranValidation" id="lstLines_Discount_DiscountBaseAmount_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Discount.DiscountBaseAmount">' + $(this).find("#lstLines_Discount_DiscountBaseAmount_" + (item) + "").text() + '</a>';
                                   htmledt += '<a class="TranValidation" id="lstLines_Master_Line_No_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Master_Line_No">' + (Number($(this).find("#lstLines_Master_Line_No_" + (item) + "").text()) + 1) + '</a>';
                                   htmledt += '</div>';
                                   htmledt += '<div class="input-group btn-group-vertical">';
                                   htmledt += '<a class="btn btn-primary btn-xs AddInvoiceLine" lineindex="' + (item + 1) + '">';
                                   htmledt += '<i class="fa fa-plus"></i>';
                                   htmledt += '</a>';
                                   htmledt += '<a class="btn btn-warning btn-xs EditInvoiceLine" lineindex="' + (item + 1) + '">';
                                   htmledt += '<i class="fa fa-edit"></i>';
                                   htmledt += '</a>';
                                   htmledt += '<a class="btn btn-danger btn-xs DeleteInvoiceLine" lineindex="' + (item + 1) + '">';
                                   htmledt += '<i class="fa fa-trash"></i>';
                                   htmledt += '</a>';
                                   htmledt += '</div>';
                                   htmledt += ' </td>';
                                   htmledt += '<td><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_Line_No_' + (item + 1) + '" extradata="' + $("#Enum_Line_No").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].Line_No">' + $(this).find("#lstLines_Line_No_" + (item) + "").text() + '</a></td>';
                                   if ($("#hdnDocFormat").val() == "UBL") {
                                       html += '<td><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstCustomer_Line_Reference_No_' + (item + 1) + '" extradata="' + $("#Enum_Customer_Line_Reference_No").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].Customer_Line_Reference_No">' + $(this).find("#lstCustomer_Line_Reference_No_" + (item) + "").text() + '</a></td>';
                                   }
                                   htmledt += '<td class="wordbreak">';
                                   htmledt += '<div><strong><a class="TranValidation EditInvoiceLine " LineIndex="' + (item + 1) + '" id="lstLines_Description_' + (item + 1) + '" extradata="' + $("#Enum_Line_Description").val() + "_" + EnumIndex + '" data-type="wysihtml5" name="lstLines[' + (item + 1) + '].Description">' + $(this).find("#lstLines_Description_" + (item) + "").text() + '</a></strong></div>';
                                   if ($("#hdnDocFormat").val() != "FINVOICE") {
                                       htmledt += '<small><a class="TranValidation EditInvoiceLine " LineIndex="' + (item + 1) + '" id="lstLines_Description2_' + (item + 1) + '" extradata="' + $("#Enum_Line_Description2").val() + "_" + EnumIndex + '" data-type="wysihtml5" name="lstLines[' + (item + 1) + '].Description2">' + $(this).find("#lstLines_Description2_" + (item) + "").text() + '</a></small><br>';
                                   }
                                   if ($("#hdnDocFormat").val() != "CXML") {
                                       htmledt += '<small><b>' + $("#lbl_EANNo").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_EANNo_' + (item + 1) + '"  name="lstLines[' + (item + 1) + '].EANNo">' + $(this).find("#lstLines_EANNo_" + (item) + "").text() + '</a> </small><br>';
                                   }
                                   htmledt += '<small><b>' + $("#lbl_CustomerItemNo").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_Customer_ItemNo_' + (item + 1) + '" extradata="' + $("#Enum_Line_Customer_ItemNo").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].Customer_ItemNo">' + $(this).find("#lstLines_Customer_ItemNo_" + (item) + "").text() + '</a> </small><br>';
                                   htmledt += '<small><b>' + $("#lbl_SupplierItemNo").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_Supplier_ItemNo_' + (item + 1) + '" extradata="' + $("#Enum_Line_Supplier_ItemNo").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].Supplier_ItemNo">' + $(this).find("#lstLines_Supplier_ItemNo_" + (item) + "").text() + '</a> </small><br>';
                                   htmledt += '<small><b>' + $("#lbl_Note").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_Notes_' + (item + 1) + '" extradata="' + $("#Enum_Line_Notes").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].Notes">' + $(this).find("#lstLines_Notes_" + (item) + "").text() + '</a> </small><br />';
                                   if ($("#hdnDocFormat").val() == "CXML" && $("#hdnDocType").val() == "Order") {
                                       htmledt += '<small><b>' + $("#lbl_labelInformation").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_labelInformation_' + (item + 1) + '" extradata="' + $("#Enum_Line_labelInformation").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].labelInformation">' + $(this).find("#lstLines_labelInformation_" + (item) + "").text() + '</a> </small><br />';
                                       htmledt += '<small><b>' + $("#lbl_labelInformation2").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_labelInformation2_' + (item + 1) + '" extradata="' + $("#Enum_Line_labelInformation2").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].labelInformation2">' + $(this).find("#lstLines_labelInformation2_" + (item) + "").text() + '</a> </small><br />';
                                       htmledt += '<small><b>' + $("#lbl_labelInformation3").val() + ':</b> <a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_labelInformation3_' + (item + 1) + '" extradata="' + $("#Enum_Line_labelInformation3").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].labelInformation3">' + $(this).find("#lstLines_labelInformation3_" + (item) + "").text() + '</a> </small><br />';
                                   }
                                   if ($("#hdnDocType").val() == "Order" && $("#hdnDocFormat").val() == "OIOUBL") {
                                       htmledt += '<small><b>' + $("#lbl_Line_DeliveryDate").val() + ': </b><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_DeliveryDate_' + (item + 1) + '" extradata="' + $("#Enum_Line_DeliveryDate").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].DeliveryDate" data-type="combodate" data-value="' + $(this).find("#lstLines_DeliveryDate_" + (item) + "").text() + '" data-format="DD-MMM-YYYY" data-viewformat="DD/MM/YYYY" data-placement="left" data-template="DD / MMM / YYYY">' + $(this).find("#lstLines_DeliveryDate_" + (item) + "").text() + '</a></small><br>';
                                   }
                                   if ($("#hdnDocType").val() == "Catalogue") {
                                       htmledt += '<small><b>Style No: </b><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_StyleNo' + (item + 1) + '" name="lstLines[' + (item + 1) + '].StyleNo">' + $(this).find("#lstLines_StyleNo" + (item) + "").text() + '</a> </small><br />';
                                       htmledt += '<small><b>Brand Code: </b><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_BrandCode_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].BrandCode">' + $(this).find("#lstLines_BrandCode_" + (item) + "").text() + '</a> &nbsp;&nbsp;</small><br />';
                                       htmledt += '<small><b>Brand Name: </b><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_BrandName_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].BrandName">' + $(this).find("#lstLines_BrandName_" + (item) + "").text() + '</a> </small><br />';
                                       htmledt += '<small><b>Season Code: </b><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_SeasonCode_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].SeasonCode">' + $(this).find("#lstLines_SeasonCode_" + (item) + "").text() + '</a> </small><br />';
                                       htmledt += '<small><b>Supplier Article Group: </b><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_SupplierArticleGroup_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].SupplierArticleGroup">' + $(this).find("#lstLines_SupplierArticleGroup_" + (item) + "").text() + '</a> </small><br />';
                                   }
                                   htmledt += '</td>';
                                   if ($("#hdnDocType").val() == "Catalogue") {
                                       htmledt += '<td class="wordbreak"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_StartDate_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].StartDate" data-type="combodate" data-value="' + $(this).find("#lstLines_StartDate_" + (item) + "").text() + '" data-format="DD-MMM-YYYY" data-viewformat="DD/MM/YYYY" data-placement="left" data-template="DD / MMM / YYYY" data-pk="1">' + $(this).find("#lstLines_StartDate_" + (item) + "").text() + '</a></td>';
                                       htmledt += '<td class="wordbreak"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_EndDate_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].EndDate" data-type="combodate" data-value="' + $(this).find("#lstLines_EndDate_" + (item) + "").text() + '" data-format="DD-MMM-YYYY" data-viewformat="DD/MM/YYYY" data-placement="left" data-template="DD / MMM / YYYY" data-pk="1">' + $(this).find("#lstLines_EndDate_" + (item) + "").text() + '</a></td>';
                                       htmledt += '<td class="text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_MinimumQuantity_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].MinimumQuantity">' + $(this).find("#lstLines_MinimumQuantity_" + (item) + "").text() + '</a></td>';
                                       htmledt += '<td class="wordbreak text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_UnitOfMeasure_' + (item + 1) + '" extradata="' + $("#Enum_Line_UnitOfMeasure").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].UnitOfMeasure">' + $(this).find("#lstLines_UnitOfMeasure_" + (item) + "").text() + '</a></td>';
                                       htmledt += '<td class="text-right"><a class="TranValidation  EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_UnitCost_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].UnitCost">' + $(this).find("#lstLines_UnitCost_" + (item) + "").text() + '</a></td>';
                                       htmledt += '<td class="text-right"><a class="TranValidation EditInvoiceLine"  lineindex="' + (item + 1) + '" id="lstLines_UnitPrice_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].UnitPrice">' + $(this).find("#lstLines_UnitPrice_" + (item) + "").text() + '</a></td>';
                                       htmledt += '<td class="text-right"><a class="TranValidation" id="lstLines_RetailPrice_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].RetailPrice">' + $(this).find("#lstLines_RetailPrice_" + (item) + "").text() + '</a></td>';
                                   }
                                   else {
                                       htmledt += '<td class="text-right"><a class="TranValidation EditInvoiceLine"  lineindex="' + (item + 1) + '" id="lstLines_Quantity_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Quantity">' + $(this).find("#lstLines_Quantity_" + (item) + "").text() + '</a></td>';
                                       htmledt += '<td class="text-right"><a class="TranValidation EditInvoiceLine"  lineindex="' + (item + 1) + '" id="lstLines_UnitPrice_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].UnitPrice">' + $(this).find("#lstLines_UnitPrice_" + (item) + "").text() + '</a></td>';
                                       if ($("#hdnDocFormat").val() == "CXML") {
                                           htmledt += '<td class="wordbreak text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_InternalUnitOfMeasure_' + (item + 1) + '" extradata="' + $("#Enum_Line_InternalUnitOfMeasure").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].InternalUnitOfMeasure">' + $(this).find("#lstLines_InternalUnitOfMeasure_" + (item) + "").text() + '</a></td>';
                                           htmledt += '<td class="wordbreak text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_UnitOfMeasure_' + (item + 1) + '" extradata="' + $("#Enum_Line_UnitOfMeasure").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].UnitOfMeasure">' + $(this).find("#lstLines_UnitOfMeasure_" + (item) + "").text() + '</a></td>';
                                           htmledt += '<td class="text-right"><a class="TranValidation EditInvoiceLine"  lineindex="' + (item + 1) + '" id="lstLines_ExternalQuantity_' + (item + 1) + '" extradata="' + $("#Enum_Line_ExternalQuantity").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].ExternalQuantity">' + $(this).find("#lstLines_ExternalQuantity_" + (item) + "").text() + '</a></td>';
                                           htmledt += '<td class="wordbreak"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_DeliveryDate_' + (item + 1) + '" extradata="' + $("#Enum_Line_DeliveryDate").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].DeliveryDate" data-type="combodate" data-value="' + $(this).find("#lstLines_DeliveryDate_" + (item) + "").text() + '" data-format="DD-MMM-YYYY" data-viewformat="DD/MM/YYYY" data-placement="left" data-template="DD / MMM / YYYY">' + $(this).find("#lstLines_DeliveryDate_" + (item) + "").text() + '</a></td>';
                                       }
                                       else if ($("#hdnDocFormat").val() == "UBL") {
                                           htmledt += '<td class="text-right"><a class="TranValidation EditInvoiceLine"  lineindex="' + (item + 1) + '" id="lstLines_ExternalQuantity_' + (item + 1) + '" extradata="' + $("#Enum_Line_ExternalQuantity").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].ExternalQuantity">' + $(this).find("#lstLines_ExternalQuantity_" + (item) + "").text() + '</a></td>';
                                           htmledt += '<td class="wordbreak text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_UnitOfMeasure_' + (item + 1) + '" extradata="' + $("#Enum_Line_UnitOfMeasure").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].UnitOfMeasure">' + $(this).find("#lstLines_UnitOfMeasure_" + (item) + "").text() + '</a></td>';
                                           htmledt += '<td class="text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_Discount_DiscountPer_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Discount.DiscountPer">' + $(this).find("#lstLines_Discount_DiscountPer_" + (item) + "").text() + '</a></td>';
                                           htmledt += '<td class="wordbreak"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_DeliveryDate_' + (item + 1) + '" extradata="' + $("#Enum_Line_DeliveryDate").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].DeliveryDate" data-type="combodate" data-value="' + $(this).find("#lstLines_DeliveryDate_" + (item) + "").text() + '" data-format="DD-MMM-YYYY" data-viewformat="DD/MM/YYYY" data-placement="left" data-template="DD / MMM / YYYY">' + $(this).find("#lstLines_DeliveryDate_" + (item) + "").text() + '</a></td>';
                                           htmledt += '<td class="text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_NetUnitPrice_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].NetUnitPrice">' + $(this).find("#lstLines_NetUnitPrice_" + (item) + "").text() + '</a></td>';
                                       }
                                       else {
                                           htmledt += '<td class="wordbreak text-right"><a class="TranValidation EditInvoiceLine" LineIndex="' + (item + 1) + '" id="lstLines_UnitOfMeasure_' + (item + 1) + '" extradata="' + $("#Enum_Line_UnitOfMeasure").val() + "_" + EnumIndex + '" name="lstLines[' + (item + 1) + '].UnitOfMeasure">' + $(this).find("#lstLines_UnitOfMeasure_" + (item) + "").text() + '</a></td>';
                                           htmledt += '<td class="text-right"><a class="TranValidation" id="lstLines_Discount_DiscountPer_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Discount.DiscountPer">' + $(this).find("#lstLines_Discount_DiscountPer_" + (item) + "").text() + '</a></td>';
                                           htmledt += '<td class="text-right"><a class="TranValidation" id="lstLines_Tax_TaxPer_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].Tax.TaxPer">' + $(this).find("#lstLines_Tax_TaxPer_" + (item) + "").text() + '</a></td>';
                                           htmledt += '<td class="text-right"><a class="TranValidation" id="lstLines_NetUnitPrice_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].NetUnitPrice">' + $(this).find("#lstLines_NetUnitPrice_" + (item) + "").text() + '</a></td>';
                                       }
                                       htmledt += '<td class="text-right"><a class="TranValidation" id="lstLines_TotalAmount_' + (item + 1) + '" name="lstLines[' + (item + 1) + '].TotalAmount">' + $(this).find("#lstLines_TotalAmount_" + (item) + "").text() + '</a></td>';
                                   }
                                   $(this).html('');
                                   $(this).html(htmledt);

                                   //$(this).prop()
                               }
                           });

                           $('#InvoiceLineTable tbody tr').eq(LineIndex - 1).after(html);

                           //$("#Row_" + LineIndex).html('');
                           //$("#Row_" + LineIndex).html(html);
                       }
                   }
                   else {
                       $("#Row_" + LineIndex).html('');
                       $("#Row_" + LineIndex).html(html);
                   }
                   if ($(".InvoiceLineHeader").hasClass("dvhide")) {
                       $(".InvoiceLineHeader").removeClass("dvhide");
                   }
                   // }
                   HB.TransactionValidationV2.ApplyXEditableToField();
                   HB.TransactionValidationV2.TotalCalculations();
                   $('html,body').animate({ scrollTop: $("#YPos").val() }, 500);
                   //$("#invoiceLineModel").modal('hide');
                   $("#invoiceLineModel").addClass("dvhide");
                   $('.invoiceLineModel-dialog').css("inset", '');
                   HB.LoginCommon.StopLoading();
               },
               onError: function (headerData, extraData) {
                   HB.LoginCommon.StopLoading();
                   HB.LoginCommon.ErrorMsg(headerData);
                   //HB.LoginCommon.ErrorMsgHighlightMultiple(headerData, extraData);
               }
           });
        }
        return false;
    }

    var getParamsAsObject = function (query) {

        query = query.substring(query.indexOf('?') + 1);

        var re = /([^&=]+)=?([^&]*)/g;
        var decodeRE = /\+/g;

        var decode = function (str) {
            return decodeURIComponent(str.replace(decodeRE, " "));
        };

        var params = { }, e;
        while (e = re.exec(query)) {
            var k = decode(e[1]), v = decode(e[2]);
            if (k.substring(k.length - 2) === '[]') {
                k = k.substring(0, k.length - 2);
                (params[k] || (params[k]= [])).push(v);
            }
            else params[k]= v;
        }

        var assign = function (obj, keyPath, value) {
            var lastKeyIndex = keyPath.length - 1;
            for (var i = 0; i < lastKeyIndex; ++i) {
                var key = keyPath[i];
                if (!(key in obj))
                    obj[key]= { }
                obj = obj[key];
            }
            obj[keyPath[lastKeyIndex]]= value;
        }

        for (var prop in params) {
            var structure = prop.split('[');
            if (structure.length > 1) {
                var levels = [];
                structure.forEach(function(item, i) {
                    var key = item.replace(/[?[\]\\ ]/g, '');
                    levels.push(key);
                });
                assign(params, levels, params[prop]);
                delete (params[prop]);
            }
        }
        return params;
    };

    this.ClearInvoiceLineData = function () {
        toastr.clear();
        //$("#invoiceLineModel").modal('hide');
        $("#invoiceLineModel").addClass("dvhide");
        $('.invoiceLineModel-dialog').css("inset", '');
        HB.TransactionValidationV2.RemoveErrorClass("Line_No");
    }

    this.RemoveErrorClass = function (Id) {
        if($("#" + Id).hasClass("error")) {
            $("#" + Id).val('');
        }
    }

    this.TotalCalculations = function (BodyLevel) {
        toastr.clear();
        RemoveAllError();
        if ($("#hdnDocFormat").val() != "CXML") {
            RM.Ajax.doCallback('/TransactionValidationV2/LineTotalCalculations?' + $("#querystring").val(), {
                data:
                    $.param($('#invoiceLines .TranValidation').map(function() {
                        return { name: this.name, value: this.text == "" ? "" : this.text };
                    })),
                onSuccess: function (data) {
                    $("#TotalItemAmount").text(data.TotalItemAmount);
                    $("#TaxAmount").text(data.TotalTaxAmount);
                    if (data.TotalTaxAmount == 0 && data.LineCount == 0)// this is the case when delete all lines and make new lines from starting, this is pending
                        $('#lstTaxString').val('[{\"TaxPer\":0.00,\"TaxAmount\":0.00,\"TaxableAmount\":' + data.TotalItemAmount + ',\"Reason\":\"\"}]');

                    if (data.LineTaxFound == true) {
                        var html = '';
                        // $(".UniqueTaxAmount").empty();
                        //for (var i = 0; i < data.UniqueTax.length; i++) {
                        //    html += '<tr class="UniqueTaxAmount">';
                        //    html += '<td><strong><a class="TranValidation" name="lstTax[' + i + '].TaxPer">' + data.UniqueTax[i].TaxPer + '</a> (%) Tax :</strong></td>';
                        //    html += '<td>';
                        //    html += '<a class="TranValidation" name="lstTax[' + i + '].TaxAmount">' + data.UniqueTax[i].TaxAmount + '</a>';
                        //    html += '<div class="dvhide"><a class="TranValidation" name="lstTax[' + i + '].TaxableAmount">' + data.UniqueTax[i].TaxableAmount + '</a></div></td>';
                        //    html += '</tr>';
                        //}
                        $('#FinalTotalTable tr:last').before(html);
                        HB.TransactionValidationV2.MainTotalCalculations();
                    }
                    else {
                        var html = '';
                        var URL = '';
                        var PostData = null;
                        if (BodyLevel == true) {
                            PostData = $.param($('.UniqueTaxAmount .TranValidation').map(function() {
                                return { name: this.name, value: this.text == "" ? "" : this.text };
                            }));
                            URL = '/TransactionValidationV2/BodyTaxCalculations?';
                        }
                        else {
                            PostData = { 'lstTaxString': $('#lstTaxString').val() };
                            URL = '/TransactionValidationV2/UniqueTaxAmount?';
                        }
                        $(".UniqueTaxAmount").empty();
                        RM.Ajax.doCallback(URL + $("#querystring").val(), {
                            data: PostData,
                            onSuccess: function (taxdata) {
                                $("#TaxAmount").text(taxdata.TotalTaxAmount);
                                for (var i = 0; i < taxdata.UniqueTax.length; i++) {
                                    html += '<tr class="UniqueTaxAmount">';
                                    html += '<td><table class="width100"><tr>';
                                    html += '<td class="col-lg-8 col-md-6 col-sm-6 col-xs-6">';
                                    html += '<a class="TranValidation dvhide fSize11" id="lstTax_' + i + '__TaxPer" name="lstTax[' + i + '].TaxPer">' + taxdata.UniqueTax[i].TaxPer + '</a>';
                                    html += '<input type="number" id="lstTax' + i + 'TaxPer" TIndex="' + i + '" class="width50 form-control input-sm text-right pull-right BodyTax"  value="' + taxdata.UniqueTax[i].TaxPer + '" maxlength="6" /></td>';
                                    html += '<td class="col-lg-4 col-md-6 col-sm-6 col-xs-6 no-padding no-margins fSize11"><strong> Tax(%) :</strong></td>';
                                    html += '</tr></table></td>';
                                    html += '<td>';
                                    html += '<a class="TranValidation fSize11" name="lstTax[' + i + '].TaxAmount" id="lstTax_' + i + '__TaxAmount">' + taxdata.UniqueTax[i].TaxAmount + '</a>';
                                    html += '<div class="dvhide"><a class="TranValidation fSize11" name="lstTax[' + i + '].TaxableAmount" id="lstTax_' + i + '__TaxableAmount">' + taxdata.UniqueTax[i].TaxableAmount + '</a></div></td>';
                                    html += '</tr>';
                                }
                                $('#FinalTotalTable tr:last').before(html);

                                $('.BodyTax').unbind().on('change', function () {
                                    var TIndex = $(this).attr("TIndex");
                                    var TaxPer = parseFloat($('#lstTax' + TIndex + 'TaxPer').val());
                                    var TaxableAmount = parseFloat($("#lstTax_" + TIndex + "__TaxableAmount").text());
                                    var TaxAmount = 0;

                                    if (TaxPer > 0)
                                        TaxAmount = TaxableAmount * TaxPer / 100;
                                    $("#lstTax_" + TIndex + "__TaxPer").text(TaxPer);
                                    $("#lstTax_" + TIndex + "__TaxAmount").text(TaxAmount);
                                    HB.TransactionValidationV2.TotalCalculations(true);
                                });
                                HB.TransactionValidationV2.MainTotalCalculations();

                            }
                        });

                        //return false;
                    }
                }
            });
        }
        else {
            var TotalAmount = 0;
            for (var i = 0; i < $("#TotalLines").val(); i++) {
                if ($("#lstLines_Deleted_" + i).text() == "False")
                    TotalAmount += parseFloat($("#lstLines_TotalAmount_" + i).text());
            }
            $("#TotalAmount").text(TotalAmount.toFixed(2));
        }
    }

    this.MainTotalCalculations = function () {
        //Total Calculations
        RM.Ajax.doCallback('/TransactionValidationV2/TotalCalculations?' + $("#querystring").val(), {
            data: { 'TotalItemAmount': $('#TotalItemAmount').text(), 'RoundingAmount': $('#txtRoundingAmount').val(), 'TotalTaxAmount': $('#TaxAmount').text(), 'DiscountPer': $('#lstDiscount0DiscountPer').val(), 'ChargePer': $('#lstCharge0ChargePer').val() },
            onSuccess: function (data) {
                $("#TotalItemAmount,#lstDiscount_0__DiscountBaseAmount,#lstCharge_0__ChargeBaseAmount").text(data.TotalItemAmount);
                $("#lstDiscount_0__DiscountAmount,#TotalDiscountAmount").text(data.TotalDiscountAmount);
                $("#lstCharge_0__ChargeAmount,#TotalChargeAmount").text(data.TotalChargeAmount);
                $("#TotalTaxAmount").text(data.TotalTaxAmount);
                $("#lstDiscount_0__DiscountPer").text($('#lstDiscount0DiscountPer').val());
                $("#lstCharge_0__ChargePer").text($('#lstCharge0ChargePer').val());
                $("#PayableAmount").text(data.PayableAmount);
            }
        });
    }

    this.SendSuppotTicketModal = function () {
        var Url = '/TransactionValidationV2/GetSupportTicketSubjectBody?' + $("#querystring").val();
        RM.Ajax.doCallback(Url, {
            data: { Gateway_Id: $("#Gateway_Id").val() },
            onSuccess: function (extraData, redirectURL) {
                HB.LoginCommon.StopLoading();
                $("#TicketSubject").val(extraData.Subject);
                $('#TicketBody').summernote('code', extraData.Body);
                $("#Support_Agent_Id").val(extraData.Support_Agent_Id);
            },
            onError: function (headerData, extraData) {
                HB.LoginCommon.StopLoading();
                HB.LoginCommon.ErrorMsg(headerData, extraData);
            }
        });
        $("#SupportTicketModal").modal();
    }

    this.SendSuppotTicket = function () {
        toastr.clear();
        var Url = '/TransactionValidationV2/SendSuppotTicket?' + $("#querystring").val();
        HB.LoginCommon.StartLoading();
        RM.Ajax.doCallback(Url, {
            data: { 'TicketSubject': $("#TicketSubject").val(), 'TicketBody': $("#TicketBody").summernote('code'), 'Support_Agent_Id': $("#Support_Agent_Id").val() },
            onSuccess: function (extraData, redirectURL) {
                HB.LoginCommon.StopLoading();
                HB.LoginCommon.SuccessMsg(extraData, '/DashBoard');
            },
            onError: function (headerData, extraData) {
                HB.LoginCommon.StopLoading();
                HB.LoginCommon.ErrorMsg(headerData, extraData);
            }
        });
        return false;
    }

    this.CancelSupportTicketModal = function () {
        toastr.clear();
        $("#SupportTicketModal").modal('hide');
        $("#TicketSubject,#TicketBody").val('');
    }

    this.ValidateFile = function () {
        if(RM.FormValidation.ValidateId("TransactionValidationForm", "formvalidationmsg")) {
            var Url = '/TransactionValidationV2/ValidateFile?' + $("#querystring").val();
            HB.LoginCommon.StartLoading();
            RM.Ajax.doCallback(Url, {
                data: $.param($('.TranValidation').map(function() {
                    return { name: this.name, value: ((this.value == "" || this.value == undefined) ? (this.text == "" ? "" : this.text) : this.value) };
                })),
                onSuccess: function (extraData, redirectURL) {
                    HB.LoginCommon.StopLoading();
                    HB.LoginCommon.SuccessMsg(extraData, redirectURL);
                    HB.TransactionValidationV2.HighlightErrors('');
                },
                onError: function (headerData, ShowMsgInPopup, Messages) {
                    HB.LoginCommon.StopLoading();
                    if (ShowMsgInPopup == 1) {
                        HB.LoginCommon.ErrorMsg(headerData);
                    }
                    else if (ShowMsgInPopup == 2) {
                        $('.TranValidation').each(function() {
                            var element = $(this);
                            $(headerData).each(function(index) {
                                if($(headerData)[index].Item4 == 0) {
                                    if ((typeof element.attr("extraData") !== 'undefined') && element.attr("extraData") == $(headerData)[index].Item1) {
                                        $(element).addClass("alert-danger");
                                    }
                                }
                                else if ((typeof element.attr("extraData") !== 'undefined')) {
                                    if (element.attr("extraData") == $(headerData)[index].Item1 + "_" + $(headerData)[index].Item4)
                                        $(element).addClass("alert-danger");

                                    //$(headerData)[index].Item1 + "_" + $(headerData)[index].Item4
                                    //element.attr("extraData") + "_" + $(headerData)[index].Item4
                                }

                            });
                        })
                        if (Messages != '') {
                            //HB.LoginCommon.ErrorMsg(Messages);
                            $("#ValidationErrorModal").modal();
                            $("#dvValidationErrors").empty();
                            $("#dvValidationErrors").html(Messages);
                            HB.TransactionValidationV2.HighlightErrors(Messages);
                        }
                    }
                    else {
                        swal({
                            title: headerData,
                            // text: $("#deletemessage").val(),
                            type: "warning",
                            showCancelButton: true,
                            confirmButtonColor: "#DD6B55",
                            confirmButtonText: "Ok",
                            cancelButtonText: "Cancel",
                            closeOnConfirm: true,
                            closeOnCancel: true
                        },
                        function (isConfirm) {
                            if(isConfirm) {
                                HB.TransactionValidationV2.SendSuppotTicketModal();
                            }
                            else {
                                //window.location.href = '/DashBoard';
                                //return false;
                            }
                        });
                    }
                }
            });
        }
        return false;
    };

    this.SaveDraft = function () {
        if(RM.FormValidation.ValidateId("TransactionValidationForm", "formvalidationmsg")) {
            var Url = '/TransactionValidationV2/SaveDraft?' + $("#querystring").val();
            HB.LoginCommon.StartLoading();
            RM.Ajax.doCallback(Url, {
                data: $.param($('.TranValidation').map(function() {
                    return { name: this.name, value: ((this.value == "" || this.value == undefined) ? (this.text == "" ? "" : this.text) : this.value) };
                })),
                onSuccess: function (extraData, redirectURL) {
                    HB.LoginCommon.StopLoading();
                    HB.LoginCommon.SuccessMsg(extraData, redirectURL);
                },
                onError: function (headerData, Messages) {
                    HB.LoginCommon.StopLoading();
                    HB.LoginCommon.ErrorMsg(headerData);
                }
            });
        }
        return false;
    };
    this.SaveReview = function () {
        if(RM.FormValidation.ValidateId("TransactionValidationForm", "formvalidationmsg")) {
            var Url = '/TransactionValidationV2/SaveReview?' + $("#querystring").val();
            HB.LoginCommon.StartLoading();
            RM.Ajax.doCallback(Url, {
                data: $.param($('.TranValidation').map(function() {
                    return { name: this.name, value: ((this.value == "" || this.value == undefined) ? (this.text == "" ? "" : this.text) : this.value) };
                })),
                onSuccess: function (extraData, redirectURL) {
                    HB.LoginCommon.StopLoading();
                    HB.LoginCommon.SuccessMsg(extraData, redirectURL);
                },
                onError: function (headerData, Messages) {
                    HB.LoginCommon.StopLoading();
                    HB.LoginCommon.ErrorMsg(headerData);
                }
            });
        }
        return false;
    };
    this.Discard = function () {
        swal({
            title: "Are you sure want to discard this document?",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: $("#btnYes").val(),
            cancelButtonText: $("#btnNo").val(),
            closeOnConfirm: true,
            closeOnCancel: true
        },
        function (isConfirm) {
            if(isConfirm) {
                var Url = '/TransactionValidationV2/Discard';
                HB.LoginCommon.StartLoading();
                RM.Ajax.doCallback(Url, {
                    data: { 'CreditNote_History_SrNo': $("#CreditNote_History_SrNo").text(), 'User_Id': $("#User_Id").text() },
                    onSuccess: function (extraData, redirectURL) {
                        HB.LoginCommon.StopLoading();
                        HB.LoginCommon.SuccessMsg(extraData, redirectURL);
                    },
                    onError: function (headerData, Messages) {
                        HB.LoginCommon.StopLoading();
                        HB.LoginCommon.ErrorMsg(headerData);
                    }
                });
            }
        });
        return false;
    };

    this.HighlightErrors = function (ValidationMessagesHTML) {
        if(ValidationMessagesHTML != '') {
            HB.TransactionValidationV2.AddRemoveHighlightErrors(ValidationMessagesHTML, "Document");
            HB.TransactionValidationV2.AddRemoveHighlightErrors(ValidationMessagesHTML, "Customer");
            HB.TransactionValidationV2.AddRemoveHighlightErrors(ValidationMessagesHTML, "Delivery");
            HB.TransactionValidationV2.AddRemoveHighlightErrors(ValidationMessagesHTML, "Billing");
            HB.TransactionValidationV2.AddRemoveHighlightErrors(ValidationMessagesHTML, "Supplier");
            HB.TransactionValidationV2.AddRemoveHighlightErrors(ValidationMessagesHTML, "Additional");
            HB.TransactionValidationV2.AddRemoveHighlightErrors(ValidationMessagesHTML, "Lines");
            HB.TransactionValidationV2.AddRemoveHighlightErrors(ValidationMessagesHTML, "Payment");
            HB.TransactionValidationV2.AddRemoveHighlightErrors(ValidationMessagesHTML, "UserDefined");
            HB.TransactionValidationV2.AddRemoveHighlightErrors(ValidationMessagesHTML, "Total");
        }
        else {
            $(".hpanel").removeClass("vred");
            $(".editorvalidation-panel-error").addClass("dvhide");
        }
    }

    this.AddRemoveHighlightErrors = function (ValidationMessagesHTML, PanelName) {
        if(ValidationMessagesHTML != '') {
            if (ValidationMessagesHTML.indexOf("<label>" + PanelName + "</label>") != - 1) {
                $("." + PanelName + "-panel").addClass("vred");
                $("." + PanelName + "-panel-error").removeClass("dvhide");
                if ($("." + PanelName + "-panel").hasClass("panel-collapse")) {
                    $("." + PanelName + "-panel").removeClass("panel-collapse");
                    $("." + PanelName + "-panel").find(".panel-body").css("display", "block");
                }
            }
            else {
                $("." + PanelName + "-panel").removeClass("vred");
                $("." + PanelName + "-panel-error").addClass("dvhide");
            }
        }
    }
    this.SaveDraftCancelCommentModal = function () {
        toastr.clear();
        $('#IgnoreComments').prop('checked', false);
        $('#DraftCommentBody').select2('enable');
        $('#DraftCommentBody').summernote('enable');
        $('#DraftCommentBody').summernote('reset');
        $("#DraftCommentBody").html('');
        $("#SaveDraftCommentModal").modal('hide');

    }
    this.SaveDraftSaveCommentModal = function () {
        var Comment = $('#DraftCommentBody').val();
        var Validation_History_Id = $('#Validation_History_Id').val();
        if ($("#IgnoreComments").is(":checked")) {
        }
        else {
            if ($('#DraftCommentBody').summernote('isEmpty') == false && Validation_History_Id > 0) {
                var Url = '/TransactionValidationV2/AddEditDraftComment';
                HB.LoginCommon.StartLoading();
                RM.Ajax.doCallback(Url, {
                    data: { 'Validation_History_Id': Validation_History_Id, 'Comment': Comment },
                    onSuccess: function (extraData, redirectURL) {
                        HB.LoginCommon.StopLoading();
                        HB.LoginCommon.SuccessMsg(extraData, '');
                    },
                    onError: function (headerData, Messages) {
                        HB.LoginCommon.StopLoading();
                        HB.LoginCommon.ErrorMsg(headerData);
                    }
                });
            }
            else {
                HB.LoginCommon.ErrorMsg("Please add comments in comment box.");
                return false;
            }
        }

        $('#IgnoreComments').prop('checked', false);
        $('#DraftCommentBody').select2('enable');
        $('#DraftCommentBody').summernote('enable');
        $('#DraftCommentBody').summernote('reset');
        $("#DraftCommentBody").html('');
        $("#SaveDraftCommentModal").modal('hide');
        HB.TransactionValidationV2.SaveDraft();
        return false;

    }

    //Created By :Nayan Hodar Date : 19-01-2021
    //This method will configure header and supplier fields from AI data
    this.GetAIData = function () {
        HB.LoginCommon.StartLoading();
        var Url = '/TransactionValidationV2/GetAIData';
        RM.Ajax.doCallback(Url, {
            data: {
                "FilePath": $("#Editor_OriginalFile_Physical").val()
            },
            onSuccess: function (AIDataList) {
                HB.LoginCommon.StopLoading();
                if (AIDataList != null && AIDataList != undefined) {
                    $.each(AIDataList, function (key, value) {
                        console.log(key + ": " + value);
                        $('input[name="' + key + '"]').val(value);
                        $('input[name="' + key + '"]').addClass('AIDetected');
                        setTimeout(function() {
                            $('input[name="' + key + '"]').removeClass('AIDetected');
                        }, 5000);
                    });
                    $('#btnGetAIData').removeClass('btn-default').addClass('btn-outline btn-success');
                    setTimeout(function() {
                        $('#btnGetAIData').removeClass('btn-outline btn-success').addClass('btn-default');
                    }, 5000);
                }
            },
            onError: function (extraData, message) {
                HB.LoginCommon.StopLoading();
                HB.LoginCommon.ErrorMsg(extraData, '');
            }
        });
        return false;
    }
}