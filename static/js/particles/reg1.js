function clickfunc(e){$(document).on("click","#"+e+"button",function(){var a=$("#"+e).val(),t=emailclient(a);console.log(a),console.log(t),pressed||$.ajax({url:"{% url 'add_email_activation' %}",data:{csrfmiddlewaretoken:"{{ csrf_token }}",email:a},async:!0,beforeSend:function(){pressed=!0,$("#"+e+"button").attr("disabled","disabled"),$("#"+e+"button").html("Отправка..."),$("#"+e).attr("disabled","disabled")},success:function(l,r){if("response"in l)$("#"+e+"button").html("Отправлено"),t[0]?($("#userclient").html('<p>Мы отправили вам письмо.</p><p>Пожалуйста, проверьте вашу почту</p><p><a href="'+t[1]+'" target="_blank">'+t[0]+"</a></p>"),console.log("Определили")):($("#userclient").html('<p class="lead">Сейчас на указанный Вами адрес <span class="text-primary">'+a+"</span> придет сообщение, содержащее ссылку для подтверждения email.<br><br>Пожалуйста, проверьте вашу почту.</p>"),console.log("Не")),$("#activateModal").modal("show");else{var o=l.error;console.log(o);var i=o.error_code;1==i&&(alert("Ошибка, пользовтель с таким email уже зарегестрирован!"),pressed=!1,$("#"+e+"button").removeAttr("disabled"),$("#"+e+"button").html("Присоединиться"),$("#"+e).removeAttr("disabled")),2==i&&(alert("Пользовтель с таким email уже активирован!"),pressed=!1,$("#"+e+"button").removeAttr("disabled"),$("#"+e+"button").html("Присоединиться"),$("#"+e).removeAttr("disabled")),3==i&&(alert("Ошибка, неверный email"),pressed=!1,$("#"+e+"button").removeAttr("disabled"),$("#"+e+"button").html("Присоединиться"),$("#"+e).removeAttr("disabled"))}},error:function(a,t,l){alert("Все плохо, расскажите нам про эту ошибку \n\r\n\r"+a+t+l),$("#"+e+"button").html("Ошибка")},type:"POST",dataType:"json"})})}function emailclient(e){var a=e.split("@"),t=a[1],l=[];switch(t){case"gmail.com":l[0]="Открыть Gmail",l[1]="https://mail.google.com/";break;case"mail.ru":l[0]="Открыть Почту Mail.Ru",l[1]="https://e.mail.ru/";break;case"list.ru":l[0]="Открыть Почту Mail.Ru (list.ru)",l[1]="https://e.mail.ru/";break;case"inbox.ru":l[0]="Открыть Почту Mail.Ru (inbox.ru)",l[1]="https://e.mail.ru/";break;case"bk.ru":l[0]="Открыть Почту Mail.Ru (bk.ru)",l[1]="https://e.mail.ru/";break;case"yandex.ru":l[0]="Открыть Почту Yandex",l[1]="https://mail.yandex.ru/";break;case"ya.ru":l[0]="Открыть Почту Yandex",l[1]="https://mail.yandex.ru/";break;case"rambler.ru":l[0]="Открыть Почту Rambler",l[1]="https://mail.rambler.ru/";break;case"e1.ru":l[0]="Открыть Почту E1.ru",l[1]="https://mail.e1.ru/";break;case"icloud.com":l[0]="Открыть iCloud Mail",l[1]="https://www.icloud.com/";break;case"me.com":l[0]="Открыть iCloud Mail",l[1]="https://www.icloud.com/";break;case"yahoo.com":l[0]="Открыть Yahoo! Mail",l[1]="https://mail.yahoo.com/";break;case"live.ru":l[0]="Открыть Outlook.com (live.ru)",l[1]="https://mail.live.com/";break;case"live.com":l[0]="Открыть Outlook.com (live.com)",l[1]="https://mail.live.com/"}return l}var pressed=!1;$(document).ready(function(){clickfunc("email")});
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInBhcnRpY2xlcy9yZWcxLmpzIl0sIm5hbWVzIjpbImNsaWNrZnVuYyIsIml0ZW0iLCIkIiwiZG9jdW1lbnQiLCJvbiIsImVtYWlsIiwidmFsIiwidXNlcl9jbGllbnQiLCJlbWFpbGNsaWVudCIsImNvbnNvbGUiLCJsb2ciLCJwcmVzc2VkIiwiYWpheCIsInVybCIsImRhdGEiLCJjc3JmbWlkZGxld2FyZXRva2VuIiwiYXN5bmMiLCJiZWZvcmVTZW5kIiwiYXR0ciIsImh0bWwiLCJzdWNjZXNzIiwidGV4dFN0YXR1cyIsIm1vZGFsIiwiZXJyb3IiLCJlcnJvcl9jb2RlIiwiYWxlcnQiLCJyZW1vdmVBdHRyIiwicmVzcG9uc2UiLCJzdGF0dXMiLCJlcnJvclRocm93biIsInR5cGUiLCJkYXRhVHlwZSIsImFyciIsInNwbGl0IiwiY2xpZW50IiwicmVzdWx0IiwicmVhZHkiXSwibWFwcGluZ3MiOiJBQTJCQSxRQUFTQSxXQUFXQyxHQUNoQkMsRUFBRUMsVUFBVUMsR0FBRyxRQUFRLElBQUlILEVBQUssU0FBVSxXQUN0QyxHQUFJSSxHQUFRSCxFQUFFLElBQUlELEdBQU1LLE1BQ3BCQyxFQUFjQyxZQUFZSCxFQUM5QkksU0FBUUMsSUFBSUwsR0FDWkksUUFBUUMsSUFBSUgsR0FDUEksU0FDRFQsRUFBRVUsTUFDRUMsSUFBSyxtQ0FDTEMsTUFDSUMsb0JBQW9CLG1CQUNwQlYsTUFBT0EsR0FFWFcsT0FBTyxFQUNQQyxXQUFZLFdBQ1JOLFNBQVUsRUFDVlQsRUFBRSxJQUFJRCxFQUFLLFVBQVVpQixLQUFLLFdBQVksWUFDdENoQixFQUFFLElBQUlELEVBQUssVUFBVWtCLEtBQUssZUFDMUJqQixFQUFFLElBQUlELEdBQU1pQixLQUFLLFdBQVksYUFFakNFLFFBQVMsU0FBVU4sRUFBTU8sR0FDckIsR0FBSSxZQUFjUCxHQUNkWixFQUFFLElBQUlELEVBQUssVUFBVWtCLEtBQUssY0FDdEJaLEVBQVksSUFDWkwsRUFBRSxlQUFlaUIsS0FBSyxxRkFBcUZaLEVBQVksR0FBRyxxQkFBcUJBLEVBQVksR0FBRyxZQUM5SkUsUUFBUUMsSUFBSSxnQkFFWlIsRUFBRSxlQUFlaUIsS0FBSyw2RUFBNkVkLEVBQU0scUhBQ3pHSSxRQUFRQyxJQUFJLE9BRWhCUixFQUFFLGtCQUFrQm9CLE1BQU0sWUFDdkIsQ0FDSCxHQUFJQyxHQUFRVCxFQUFZLEtBQ3hCTCxTQUFRQyxJQUFJYSxFQUNaLElBQUlDLEdBQWFELEVBQWtCLFVBQ2pCLElBQWRDLElBQ0FDLE1BQU0sMERBQ05kLFNBQVUsRUFDVlQsRUFBRSxJQUFJRCxFQUFLLFVBQVV5QixXQUFXLFlBQ2hDeEIsRUFBRSxJQUFJRCxFQUFLLFVBQVVrQixLQUFLLGtCQUMxQmpCLEVBQUUsSUFBSUQsR0FBTXlCLFdBQVcsYUFFVCxHQUFkRixJQUNBQyxNQUFNLDhDQUNOZCxTQUFVLEVBQ1ZULEVBQUUsSUFBSUQsRUFBSyxVQUFVeUIsV0FBVyxZQUNoQ3hCLEVBQUUsSUFBSUQsRUFBSyxVQUFVa0IsS0FBSyxrQkFDMUJqQixFQUFFLElBQUlELEdBQU15QixXQUFXLGFBRVQsR0FBZEYsSUFDQUMsTUFBTSwwQkFDTmQsU0FBVSxFQUNWVCxFQUFFLElBQUlELEVBQUssVUFBVXlCLFdBQVcsWUFDaEN4QixFQUFFLElBQUlELEVBQUssVUFBVWtCLEtBQUssa0JBQzFCakIsRUFBRSxJQUFJRCxHQUFNeUIsV0FBVyxlQUluQ0gsTUFBTyxTQUFVSSxFQUFVQyxFQUFRQyxHQUMvQkosTUFBTSxvREFBc0RFLEVBQVdDLEVBQVNDLEdBQ2hGM0IsRUFBRSxJQUFJRCxFQUFLLFVBQVVrQixLQUFLLFdBRTlCVyxLQUFNLE9BQ05DLFNBQVUsV0FNMUIsUUFBU3ZCLGFBQVlQLEdBQ2pCLEdBQUkrQixHQUFNL0IsRUFBS2dDLE1BQU0sS0FDakJDLEVBQVNGLEVBQUksR0FDYkcsSUFDSixRQUFRRCxHQUNKLElBQUssWUFDREMsRUFBTyxHQUFLLGdCQUNaQSxFQUFPLEdBQUssMEJBQ1osTUFLSixLQUFLLFVBQ0RBLEVBQU8sR0FBSyx3QkFDWkEsRUFBTyxHQUFLLG9CQUNaLE1BQ0osS0FBSyxVQUNEQSxFQUFPLEdBQUssa0NBQ1pBLEVBQU8sR0FBSyxvQkFDWixNQUNKLEtBQUssV0FDREEsRUFBTyxHQUFLLG1DQUNaQSxFQUFPLEdBQUssb0JBQ1osTUFDSixLQUFLLFFBQ0RBLEVBQU8sR0FBSyxnQ0FDWkEsRUFBTyxHQUFLLG9CQUNaLE1BQ0osS0FBSyxZQUNEQSxFQUFPLEdBQUssdUJBQ1pBLEVBQU8sR0FBSyx5QkFDWixNQUNKLEtBQUssUUFDREEsRUFBTyxHQUFLLHVCQUNaQSxFQUFPLEdBQUsseUJBQ1osTUFDSixLQUFLLGFBQ0RBLEVBQU8sR0FBSyx3QkFDWkEsRUFBTyxHQUFLLDBCQUNaLE1BQ0osS0FBSyxRQUNEQSxFQUFPLEdBQUssc0JBQ1pBLEVBQU8sR0FBSyxxQkFDWixNQUNKLEtBQUssYUFDREEsRUFBTyxHQUFLLHNCQUNaQSxFQUFPLEdBQUsseUJBQ1osTUFDSixLQUFLLFNBQ0RBLEVBQU8sR0FBSyxzQkFDWkEsRUFBTyxHQUFLLHlCQUNaLE1BQ0osS0FBSyxZQUNEQSxFQUFPLEdBQUssc0JBQ1pBLEVBQU8sR0FBSyx5QkFDWixNQUNKLEtBQUssVUFDREEsRUFBTyxHQUFLLGdDQUNaQSxFQUFPLEdBQUssd0JBQ1osTUFDSixLQUFLLFdBQ0RBLEVBQU8sR0FBSyxpQ0FDWkEsRUFBTyxHQUFLLHlCQUlwQixNQUFPQSxHQWhLWCxHQUFJeEIsVUFBVSxDQUNkVCxHQUFFQyxVQUFVaUMsTUFBTSxXQUVkcEMsVUFBVSIsImZpbGUiOiJwYXJ0aWNsZXMvcmVnMS5qcyIsInNvdXJjZXNDb250ZW50IjpbIi8qKlxuICogQ3JlYXRlZCBieSB2aXRhbGl5aGFyY2hlbmtvIG9uIDE2LjA2LjE1LlxuICovXG52YXIgcHJlc3NlZCA9IGZhbHNlO1xuJChkb2N1bWVudCkucmVhZHkoZnVuY3Rpb24oKSB7XG4gICAgLy9pbnB1dGZ1bmMoJ2VtYWlsJyk7XG4gICAgY2xpY2tmdW5jKCdlbWFpbCcpO1xufSk7XG5cbi8vZnVuY3Rpb24gaW5wdXRmdW5jIChpdGVtKSB7XG4vLyAgICAkKGRvY3VtZW50KS5vbignaW5wdXQnLCcjJytpdGVtLCBmdW5jdGlvbigpe1xuLy8gICAgICAgIGlmKCQodGhpcykudmFsKCkgIT0gJycpIHtcbi8vICAgICAgICAgICAgdmFyIHBhdHRlcm4gPSAvXihbYS16MC05X1xcLi1dKStAW2EtejAtOS1dK1xcLihbYS16XXsyLDR9XFwuKT9bYS16XXsyLDR9JC9pO1xuLy8gICAgICAgICAgICBpZihwYXR0ZXJuLnRlc3QoJCh0aGlzKS52YWwoKSkpe1xuLy8gICAgICAgICAgICAgICAgJCh0aGlzKS5jc3Moeydib3JkZXInIDogJzFweCBzb2xpZCAjNTY5YjQ0J30pO1xuLy8gICAgICAgICAgICAgICAgJCgnIycraXRlbSsnYnV0dG9uJykucmVtb3ZlQXR0cignZGlzYWJsZWQnKTtcbi8vICAgICAgICAgICAgfSBlbHNlIHtcbi8vICAgICAgICAgICAgICAgICQodGhpcykuY3NzKHsnYm9yZGVyJyA6ICcxcHggc29saWQgI2ZmMDAwMCd9KTtcbi8vICAgICAgICAgICAgICAgICQoJyMnK2l0ZW0rJ2J1dHRvbicpLmF0dHIoJ2Rpc2FibGVkJywgJ2Rpc2FibGVkJyk7XG4vLyAgICAgICAgICAgIH1cbi8vICAgICAgICB9IGVsc2Uge1xuLy8gICAgICAgICAgICAkKHRoaXMpLmNzcyh7J2JvcmRlcicgOiAnMXB4IHNvbGlkICNmZjAwMDAnfSk7XG4vLyAgICAgICAgICAgICQoJyMnK2l0ZW0rJ2J1dHRvbicpLmF0dHIoJ2Rpc2FibGVkJywgJ2Rpc2FibGVkJyk7XG4vLyAgICAgICAgfTtcbi8vICAgIH0pO1xuLy99O1xuXG5mdW5jdGlvbiBjbGlja2Z1bmMgKGl0ZW0pIHtcbiAgICAkKGRvY3VtZW50KS5vbignY2xpY2snLCcjJytpdGVtKydidXR0b24nLCBmdW5jdGlvbigpe1xuICAgICAgICB2YXIgZW1haWwgPSAkKCcjJytpdGVtKS52YWwoKTtcbiAgICAgICAgdmFyIHVzZXJfY2xpZW50ID0gZW1haWxjbGllbnQoZW1haWwpO1xuICAgICAgICBjb25zb2xlLmxvZyhlbWFpbCk7XG4gICAgICAgIGNvbnNvbGUubG9nKHVzZXJfY2xpZW50KTtcbiAgICAgICAgaWYgKCFwcmVzc2VkKSB7XG4gICAgICAgICAgICAkLmFqYXgoe1xuICAgICAgICAgICAgICAgIHVybDogXCJ7JSB1cmwgJ2FkZF9lbWFpbF9hY3RpdmF0aW9uJyAlfVwiLFxuICAgICAgICAgICAgICAgIGRhdGE6IHtcbiAgICAgICAgICAgICAgICAgICAgY3NyZm1pZGRsZXdhcmV0b2tlbjone3sgY3NyZl90b2tlbiB9fScsXG4gICAgICAgICAgICAgICAgICAgIGVtYWlsOiBlbWFpbFxuICAgICAgICAgICAgICAgIH0sXG4gICAgICAgICAgICAgICAgYXN5bmM6IHRydWUsXG4gICAgICAgICAgICAgICAgYmVmb3JlU2VuZDogZnVuY3Rpb24oKSB7XG4gICAgICAgICAgICAgICAgICAgIHByZXNzZWQgPSB0cnVlO1xuICAgICAgICAgICAgICAgICAgICAkKCcjJytpdGVtKydidXR0b24nKS5hdHRyKCdkaXNhYmxlZCcsICdkaXNhYmxlZCcpO1xuICAgICAgICAgICAgICAgICAgICAkKCcjJytpdGVtKydidXR0b24nKS5odG1sKCfQntGC0L/RgNCw0LLQutCwLi4uJyk7XG4gICAgICAgICAgICAgICAgICAgICQoJyMnK2l0ZW0pLmF0dHIoJ2Rpc2FibGVkJywgJ2Rpc2FibGVkJyk7XG4gICAgICAgICAgICAgICAgfSxcbiAgICAgICAgICAgICAgICBzdWNjZXNzOiBmdW5jdGlvbiAoZGF0YSwgdGV4dFN0YXR1cykge1xuICAgICAgICAgICAgICAgICAgICBpZiAoJ3Jlc3BvbnNlJyBpbiBkYXRhKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAkKCcjJytpdGVtKydidXR0b24nKS5odG1sKCfQntGC0L/RgNCw0LLQu9C10L3QvicpO1xuICAgICAgICAgICAgICAgICAgICAgICAgaWYgKHVzZXJfY2xpZW50WzBdKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgJCgnI3VzZXJjbGllbnQnKS5odG1sKCc8cD7QnNGLINC+0YLQv9GA0LDQstC40LvQuCDQstCw0Lwg0L/QuNGB0YzQvNC+LjwvcD48cD7Qn9C+0LbQsNC70YPQudGB0YLQsCwg0L/RgNC+0LLQtdGA0YzRgtC1INCy0LDRiNGDINC/0L7Rh9GC0YM8L3A+PHA+PGEgaHJlZj1cIicrdXNlcl9jbGllbnRbMV0rJ1wiIHRhcmdldD1cIl9ibGFua1wiPicrdXNlcl9jbGllbnRbMF0rJzwvYT48L3A+Jyk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgY29uc29sZS5sb2coJ9Ce0L/RgNC10LTQtdC70LjQu9C4Jyk7XG4gICAgICAgICAgICAgICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICQoJyN1c2VyY2xpZW50JykuaHRtbCgnPHAgY2xhc3M9XCJsZWFkXCI+0KHQtdC50YfQsNGBINC90LAg0YPQutCw0LfQsNC90L3Ri9C5INCS0LDQvNC4INCw0LTRgNC10YEgPHNwYW4gY2xhc3M9XCJ0ZXh0LXByaW1hcnlcIj4nK2VtYWlsKyc8L3NwYW4+INC/0YDQuNC00LXRgiDRgdC+0L7QsdGJ0LXQvdC40LUsINGB0L7QtNC10YDQttCw0YnQtdC1INGB0YHRi9C70LrRgyDQtNC70Y8g0L/QvtC00YLQstC10YDQttC00LXQvdC40Y8gZW1haWwuPGJyPjxicj7Qn9C+0LbQsNC70YPQudGB0YLQsCwg0L/RgNC+0LLQtdGA0YzRgtC1INCy0LDRiNGDINC/0L7Rh9GC0YMuPC9wPicpO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNvbnNvbGUubG9nKCfQndC1Jyk7XG4gICAgICAgICAgICAgICAgICAgICAgICB9O1xuICAgICAgICAgICAgICAgICAgICAgICAgJCgnI2FjdGl2YXRlTW9kYWwnKS5tb2RhbCgnc2hvdycpO1xuICAgICAgICAgICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICAgICAgICAgICAgdmFyIGVycm9yID0gZGF0YVsnZXJyb3InXTtcbiAgICAgICAgICAgICAgICAgICAgICAgIGNvbnNvbGUubG9nKGVycm9yKTtcbiAgICAgICAgICAgICAgICAgICAgICAgIHZhciBlcnJvcl9jb2RlID0gZXJyb3JbJ2Vycm9yX2NvZGUnXTtcbiAgICAgICAgICAgICAgICAgICAgICAgIGlmIChlcnJvcl9jb2RlID09IDEpe1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGFsZXJ0KCfQntGI0LjQsdC60LAsINC/0L7Qu9GM0LfQvtCy0YLQtdC70Ywg0YEg0YLQsNC60LjQvCBlbWFpbCDRg9C20LUg0LfQsNGA0LXQs9C10YHRgtGA0LjRgNC+0LLQsNC9IScpXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJlc3NlZCA9IGZhbHNlO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICQoJyMnK2l0ZW0rJ2J1dHRvbicpLnJlbW92ZUF0dHIoJ2Rpc2FibGVkJyk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgJCgnIycraXRlbSsnYnV0dG9uJykuaHRtbCgn0J/RgNC40YHQvtC10LTQuNC90LjRgtGM0YHRjycpO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICQoJyMnK2l0ZW0pLnJlbW92ZUF0dHIoJ2Rpc2FibGVkJyk7XG4gICAgICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgICAgICBpZiAoZXJyb3JfY29kZSA9PSAyKXtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBhbGVydCgn0J/QvtC70YzQt9C+0LLRgtC10LvRjCDRgSDRgtCw0LrQuNC8IGVtYWlsINGD0LbQtSDQsNC60YLQuNCy0LjRgNC+0LLQsNC9IScpXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJlc3NlZCA9IGZhbHNlO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICQoJyMnK2l0ZW0rJ2J1dHRvbicpLnJlbW92ZUF0dHIoJ2Rpc2FibGVkJyk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgJCgnIycraXRlbSsnYnV0dG9uJykuaHRtbCgn0J/RgNC40YHQvtC10LTQuNC90LjRgtGM0YHRjycpO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICQoJyMnK2l0ZW0pLnJlbW92ZUF0dHIoJ2Rpc2FibGVkJyk7XG4gICAgICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgICAgICBpZiAoZXJyb3JfY29kZSA9PSAzKXtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBhbGVydCgn0J7RiNC40LHQutCwLCDQvdC10LLQtdGA0L3Ri9C5IGVtYWlsJylcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmVzc2VkID0gZmFsc2U7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgJCgnIycraXRlbSsnYnV0dG9uJykucmVtb3ZlQXR0cignZGlzYWJsZWQnKTtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAkKCcjJytpdGVtKydidXR0b24nKS5odG1sKCfQn9GA0LjRgdC+0LXQtNC40L3QuNGC0YzRgdGPJyk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgJCgnIycraXRlbSkucmVtb3ZlQXR0cignZGlzYWJsZWQnKTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIH0sXG4gICAgICAgICAgICAgICAgZXJyb3I6IGZ1bmN0aW9uIChyZXNwb25zZSwgc3RhdHVzLCBlcnJvclRocm93bikge1xuICAgICAgICAgICAgICAgICAgICBhbGVydCgn0JLRgdC1INC/0LvQvtGF0L4sINGA0LDRgdGB0LrQsNC20LjRgtC1INC90LDQvCDQv9GA0L4g0Y3RgtGDINC+0YjQuNCx0LrRgyBcXG5cXHJcXG5cXHInICsgcmVzcG9uc2UgKyBzdGF0dXMgKyBlcnJvclRocm93bik7XG4gICAgICAgICAgICAgICAgICAgICQoJyMnK2l0ZW0rJ2J1dHRvbicpLmh0bWwoJ9Ce0YjQuNCx0LrQsCcpO1xuICAgICAgICAgICAgICAgIH0sXG4gICAgICAgICAgICAgICAgdHlwZTogXCJQT1NUXCIsXG4gICAgICAgICAgICAgICAgZGF0YVR5cGU6IFwianNvblwiXG4gICAgICAgICAgICB9KTtcbiAgICAgICAgfVxuICAgIH0pO1xufTtcblxuZnVuY3Rpb24gZW1haWxjbGllbnQoaXRlbSkge1xuICAgIHZhciBhcnIgPSBpdGVtLnNwbGl0KCdAJyk7XG4gICAgdmFyIGNsaWVudCA9IGFyclsxXTtcbiAgICB2YXIgcmVzdWx0ID0gW107XG4gICAgc3dpdGNoIChjbGllbnQpIHtcbiAgICAgICAgY2FzZSAnZ21haWwuY29tJzpcbiAgICAgICAgICAgIHJlc3VsdFswXSA9ICfQntGC0LrRgNGL0YLRjCBHbWFpbCc7XG4gICAgICAgICAgICByZXN1bHRbMV0gPSAnaHR0cHM6Ly9tYWlsLmdvb2dsZS5jb20vJztcbiAgICAgICAgICAgIGJyZWFrXG4gICAgICAgIC8vIGNhc2UgJ3Nwb3J0Y291cnRzLnJ1JzpcbiAgICAgICAgLy8gICByZXN1bHRbMF0gPSAn0J7RgtC60YDRi9GC0YwgR21haWwnO1xuICAgICAgICAvLyAgIHJlc3VsdFsxXSA9ICdodHRwczovL21haWwuZ29vZ2xlLmNvbS8nO1xuICAgICAgICAvLyAgIGJyZWFrXG4gICAgICAgIGNhc2UgJ21haWwucnUnOlxuICAgICAgICAgICAgcmVzdWx0WzBdID0gJ9Ce0YLQutGA0YvRgtGMINCf0L7Rh9GC0YMgTWFpbC5SdSc7XG4gICAgICAgICAgICByZXN1bHRbMV0gPSAnaHR0cHM6Ly9lLm1haWwucnUvJztcbiAgICAgICAgICAgIGJyZWFrXG4gICAgICAgIGNhc2UgJ2xpc3QucnUnOlxuICAgICAgICAgICAgcmVzdWx0WzBdID0gJ9Ce0YLQutGA0YvRgtGMINCf0L7Rh9GC0YMgTWFpbC5SdSAobGlzdC5ydSknO1xuICAgICAgICAgICAgcmVzdWx0WzFdID0gJ2h0dHBzOi8vZS5tYWlsLnJ1Lyc7XG4gICAgICAgICAgICBicmVha1xuICAgICAgICBjYXNlICdpbmJveC5ydSc6XG4gICAgICAgICAgICByZXN1bHRbMF0gPSAn0J7RgtC60YDRi9GC0Ywg0J/QvtGH0YLRgyBNYWlsLlJ1IChpbmJveC5ydSknO1xuICAgICAgICAgICAgcmVzdWx0WzFdID0gJ2h0dHBzOi8vZS5tYWlsLnJ1Lyc7XG4gICAgICAgICAgICBicmVha1xuICAgICAgICBjYXNlICdiay5ydSc6XG4gICAgICAgICAgICByZXN1bHRbMF0gPSAn0J7RgtC60YDRi9GC0Ywg0J/QvtGH0YLRgyBNYWlsLlJ1IChiay5ydSknO1xuICAgICAgICAgICAgcmVzdWx0WzFdID0gJ2h0dHBzOi8vZS5tYWlsLnJ1Lyc7XG4gICAgICAgICAgICBicmVha1xuICAgICAgICBjYXNlICd5YW5kZXgucnUnOlxuICAgICAgICAgICAgcmVzdWx0WzBdID0gJ9Ce0YLQutGA0YvRgtGMINCf0L7Rh9GC0YMgWWFuZGV4JztcbiAgICAgICAgICAgIHJlc3VsdFsxXSA9ICdodHRwczovL21haWwueWFuZGV4LnJ1Lyc7XG4gICAgICAgICAgICBicmVha1xuICAgICAgICBjYXNlICd5YS5ydSc6XG4gICAgICAgICAgICByZXN1bHRbMF0gPSAn0J7RgtC60YDRi9GC0Ywg0J/QvtGH0YLRgyBZYW5kZXgnO1xuICAgICAgICAgICAgcmVzdWx0WzFdID0gJ2h0dHBzOi8vbWFpbC55YW5kZXgucnUvJztcbiAgICAgICAgICAgIGJyZWFrXG4gICAgICAgIGNhc2UgJ3JhbWJsZXIucnUnOlxuICAgICAgICAgICAgcmVzdWx0WzBdID0gJ9Ce0YLQutGA0YvRgtGMINCf0L7Rh9GC0YMgUmFtYmxlcic7XG4gICAgICAgICAgICByZXN1bHRbMV0gPSAnaHR0cHM6Ly9tYWlsLnJhbWJsZXIucnUvJztcbiAgICAgICAgICAgIGJyZWFrXG4gICAgICAgIGNhc2UgJ2UxLnJ1JzpcbiAgICAgICAgICAgIHJlc3VsdFswXSA9ICfQntGC0LrRgNGL0YLRjCDQn9C+0YfRgtGDIEUxLnJ1JztcbiAgICAgICAgICAgIHJlc3VsdFsxXSA9ICdodHRwczovL21haWwuZTEucnUvJztcbiAgICAgICAgICAgIGJyZWFrXG4gICAgICAgIGNhc2UgJ2ljbG91ZC5jb20nOlxuICAgICAgICAgICAgcmVzdWx0WzBdID0gJ9Ce0YLQutGA0YvRgtGMIGlDbG91ZCBNYWlsJztcbiAgICAgICAgICAgIHJlc3VsdFsxXSA9ICdodHRwczovL3d3dy5pY2xvdWQuY29tLyc7XG4gICAgICAgICAgICBicmVha1xuICAgICAgICBjYXNlICdtZS5jb20nOlxuICAgICAgICAgICAgcmVzdWx0WzBdID0gJ9Ce0YLQutGA0YvRgtGMIGlDbG91ZCBNYWlsJztcbiAgICAgICAgICAgIHJlc3VsdFsxXSA9ICdodHRwczovL3d3dy5pY2xvdWQuY29tLyc7XG4gICAgICAgICAgICBicmVha1xuICAgICAgICBjYXNlICd5YWhvby5jb20nOlxuICAgICAgICAgICAgcmVzdWx0WzBdID0gJ9Ce0YLQutGA0YvRgtGMIFlhaG9vISBNYWlsJztcbiAgICAgICAgICAgIHJlc3VsdFsxXSA9ICdodHRwczovL21haWwueWFob28uY29tLyc7XG4gICAgICAgICAgICBicmVha1xuICAgICAgICBjYXNlICdsaXZlLnJ1JzpcbiAgICAgICAgICAgIHJlc3VsdFswXSA9ICfQntGC0LrRgNGL0YLRjCBPdXRsb29rLmNvbSAobGl2ZS5ydSknO1xuICAgICAgICAgICAgcmVzdWx0WzFdID0gJ2h0dHBzOi8vbWFpbC5saXZlLmNvbS8nO1xuICAgICAgICAgICAgYnJlYWtcbiAgICAgICAgY2FzZSAnbGl2ZS5jb20nOlxuICAgICAgICAgICAgcmVzdWx0WzBdID0gJ9Ce0YLQutGA0YvRgtGMIE91dGxvb2suY29tIChsaXZlLmNvbSknO1xuICAgICAgICAgICAgcmVzdWx0WzFdID0gJ2h0dHBzOi8vbWFpbC5saXZlLmNvbS8nO1xuICAgICAgICAgICAgYnJlYWtcbiAgICAgICAgZGVmYXVsdDpcbiAgICB9O1xuICAgIHJldHVybiByZXN1bHQ7XG59Il0sInNvdXJjZVJvb3QiOiIvc291cmNlLyJ9