/**
 * Created by vitaliyharchenko on 31.07.15.
 */
var avatar_url = "{{ avatar_url }}";
$(document).ready(function() {
    if (vkuserid != "") {
        $('#jasny-url').attr('value', avatar_url);
    }
});