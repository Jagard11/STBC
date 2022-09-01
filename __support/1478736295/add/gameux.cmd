@ECHO OFF
SET regpath="HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\GameUX\ServiceLocation"
REG ADD %regpath% /v "Games" /t REG_SZ /d "localhost" /f
REG ADD %regpath% /v "Games_backup" /t REG_SZ /d "https://games.metaservices.microsoft.com/games/SGamesWebService.asmx" /f
exit