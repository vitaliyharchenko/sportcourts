/**
 * Created by vitaliyharchenko on 16.06.15.
 */
var vkuserid = "{{ vkuserid }}";
var avatar_url = "{{ avatar_url }}";
$(document).ready(function() {
    if (vkuserid != "") {
        $('#jasny-url').attr('value', avatar_url);
    }
});