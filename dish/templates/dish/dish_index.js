$(document).ready(function() {

     $('button[id="sendDinner2"]').on('click', function(){
        $('#status').text("Статус відправки замовлення у групу: ")
        var dishesList = $('textarea[name="final"]').val();
        var textToSend ="Замовлення через http://nuriyevn.pythonanywhere.com/dish/!%0A%0A"
        textToSend += $('#person').val() + "%0A%0A"
        textToSend += dishesList

         $.ajax({
            url: 'https://api.telegram.org/bot800787990:AAHo4OBTilvKuOiEpInOvICNFIfEw_rAYek/getMe',
            type:'GET',
            // 128501515
            data: null,
            complete: function(event)
            {
                console.log(event.responseText);
            }

        });

        textToSend = textToSend.replace(/(?:\r\n|\r|\n)/g, '%0A');

        if (dishesList.trim().length > 0)
            $.ajax({
                url: 'https://api.telegram.org/bot800787990:AAHo4OBTilvKuOiEpInOvICNFIfEw_rAYek/sendMessage',
                type:'GET',
                // 128501515 - тестова група
                // 254455448 -  група обіди
                data: 'chat_id=-254455448&parseMode=html&text=' + textToSend,
                complete: function(event)
                {
                    console.log(event)
                }
            });

        else
        {
            $('#status').text("Пусте замовлення")
        }
        console.log("Send pressed")
     });

     $('input[type="radio"]').on('click', function(){
        var final = '';
        $('#sum').attr('style', "color:green;");

        var ids = [];
        $('input:checked').each(function(){

            if (parseInt(this.value, 10) !== 0){
                final += $(this)[0].nextSibling.textContent;
                final += '\n'
                console.log($(this)[0].nextSibling);
                ids.push($(this).val())
            }
        })

        console.log(ids);
        $.ajax({
            url: '/dish/calculate',
            data: { ids },
            type:"GET",
            complete: function(event){

                var old = 'Сума: ';
                if (parseFloat(event.responseText) > 160.0)
                    $('#sum').attr('style', "color:red;");

                $('#sum').text(old + event.responseText + ' грн.');
            }
        })

        $('textarea[name="final"]').val(final);
     })

    $('input[type="button"][id="addonClear"]').on('click', function(){
        $('input[name="addon"][value="0"]')[0].click();
    });


    $('input[type="button"][id="main_dishClear"]').on('click', function(){
        $('input[name="main_dish"][value="0"]')[0].click();
    });


    $('input[type="button"][id="side_dishClear"]').on('click', function(){
            $('input[name="side_dish"][value="0"]')[0].click();
    });

    $('input[type="button"][id="sauce_dishClear"]').on('click', function(){
        $('input[name="sauce_dish"][value="0"]')[0].click();
    });

    $('input[type="button"][id="drinkClear"]').on('click', function(){
        $('input[name="drink"][value="0"]')[0].click();
    });

    $('input[type="button"][id="saladClear"]').on('click', function(){
        $('input[name="salad"][value="0"]')[0].click();
    });

    $('input[type="button"][id="soupClear"]').on('click', function(){
        $('input[name="soup"][value="0"]')[0].click();
    });

    $('input[type="button"][id="bruschettaClear"]').on('click', function(){
        $('input[name="bruschetta"][value="0"]')[0].click();
    });

     document.getElementById("copyButton").addEventListener("click", function() {
    copyToClipboard(document.getElementById("copyTarget"));
    });

    function copyToClipboard(elem) {
          // create hidden text element, if it doesn't already exist
        var targetId = "_hiddenCopyText_";
        var isInput = elem.tagName === "INPUT" || elem.tagName === "TEXTAREA";
        var origSelectionStart, origSelectionEnd;
        if (isInput) {
            // can just use the original source element for the selection and copy
            target = elem;
            origSelectionStart = elem.selectionStart;
            origSelectionEnd = elem.selectionEnd;
        } else {
            // must use a temporary form element for the selection and copy
            target = document.getElementById(targetId);
            if (!target) {
                var target = document.createElement("textarea");
                target.style.position = "absolute";
                target.style.left = "-9999px";
                target.style.top = "0";
                target.id = targetId;
                document.body.appendChild(target);
            }
            target.textContent = elem.textContent;
        }
        // select the content
        var currentFocus = document.activeElement;
        target.focus();
        target.setSelectionRange(0, target.value.length);

        // copy the selection
        var succeed;
        try {
              succeed = document.execCommand("copy");
        } catch(e) {
            succeed = false;
        }
        // restore original focus
        if (currentFocus && typeof currentFocus.focus === "function") {
            currentFocus.focus();
        }

        if (isInput) {
            // restore prior selection
            elem.setSelectionRange(origSelectionStart, origSelectionEnd);
        } else {
            // clear temporary content
            target.textContent = "";
        }
        return succeed;
    }
});
