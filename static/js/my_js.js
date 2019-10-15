$(document).ready(function () {
    $("#flash_message").hide();
    $("button.close").click(function () {
        $("#flash_message").hide();
    });
    $("#post_message").click(function () {
        let name = $("input[name='name']").val();
        let message = $("textarea[name='message']").val();
        if (name == '' || message == '') {
            $("#flash_message").show();
        } else if (message.length > 200) {
            $("#flash_message").show();
            $(".alert").children("p").text("输入内容过长");
        } else {
            $("#flash_message").hide();
            $("#message_form").submit();
        }
    });
});