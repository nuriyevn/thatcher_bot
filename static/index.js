$(document).ready(function() {
     $('button[id="sendDinner"]').on('click', function(){
        $('#status').text("Статус відправки замовлення у групу: ")
        var dishesList = $('textarea[name="final"]').val();
        var textToSend ="Увага! Тестове замовлення через telegram bot!%0A%0A"
        textToSend += dishesList
        textToSend = textToSend.replace(/(?:\r\n|\r|\n)/g, '%0A');

        if (dishesList.trim().length > 0)
            $.ajax({
                url: 'https://api.telegram.org/bot800787990:AAHo4OBTilvKuOiEpInOvICNFIfEw_rAYek/sendMessage',
                type:'GET',
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

     $('input').on('click', function(){
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

                $('#sum').text(old + event.responseText);
            }
        })

        $('textarea[name="final"]').val(final);
     })
});