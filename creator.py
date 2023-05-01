import json
import secrets
import threading
import sys
import requests
import re
import base64
import hmac
import hashlib
import string
import random
import os
import colorama
import urllib3 
from uuid import uuid4 
from colorama import Fore
import time as te
from json import loads 
from re import search 
from threading import Thread
urllib3.disable_warnings()
thread_lock = threading.Lock()
dick : dict = json.load(open("config.json"))
ua : str = dick["user-agent"]
locale : str = dick["locale"]
proxies = dick["proxies"]

request_exceptions = (requests.exceptions.ProxyError,requests.exceptions.Timeout,requests.exceptions.SSLError)
prePareCartFlights = ['sc_appendconversiontype', 'sc_showvalidpis', 'sc_scdstextdirection', 'sc_optimizecheckoutload', 'sc_purchasedblockedby', 'sc_passthroughculture', 'sc_showcanceldisclaimerdefaultv1', 'sc_redirecttosignin', 'sc_paymentpickeritem', 'sc_cleanreducercode', 'sc_dimealipaystylingfix', 'sc_promocode', 'sc_onedrivedowngrade', 'sc_newooslogiconcart', 'sc_optionalcatalogclienttype', 'sc_klarna', 'sc_hidecontactcheckbox', 'sc_preparecheckoutrefactor', 'sc_checkoutklarna', 'sc_currencyformattingpkg', 'sc_fullpageredirectionforasyncpi', 'sc_xaaconversionerror', 'sc_promocodefeature-web-desktop', 'sc_eligibilityproducts', 'sc_disabledpaymentoption',
'sc_enablecartcreationerrorparsing', 'sc_purchaseblock', 'sc_returnoospsatocart', 'sc_dynamicseligibility', 'sc_usebuynowonlyinternalendpoint', 'sc_removemoreless', 'sc_renewalsubscriptionselector', 'sc_hidexdledd', 'sc_militaryshippingurl', 'sc_xboxdualleaf', 'sc_japanlegalterms', 'sc_multiplesubscriptions', 'sc_loweroriginalprice', 'sc_xaatovalenciastring', 'sc_cannotbuywarrantyalone', 'sc_showminimalfooteroncheckout', 'sc_checkoutdowngrade', 'sc_checkoutcontainsiaps', 'sc_localizedtax', 'sc_officescds', 'sc_disableupgradetrycheckout', 'sc_extendPageTagToOverride', 'sc_checkoutscenariotelemetry', 'sc_skipselectpi', 'sc_allowmpesapi', 'sc_purchasestatusmessage', 'sc_storetermslink', 'sc_postorderinfolineitemmessage', 'sc_addpaymentfingerprinttagging', 'sc_shippingallowlist', 'sc_emptyresultcheck', 'sc_dualleaf', 'sc_riskyxtoken', 'sc_abandonedretry', 'sc_testflightbuynow', 'sc_addshippingmethodtelemetry', 'sc_leaficons', 'sc_newspinneroverlay', 'sc_paymentinstrumenttypeandfamily', 'sc_addsitename', 'sc_disallowalipayforcheckout', 'sc_checkoutsignintelemetry', 'sc_prominenteddchange', 'sc_disableshippingaddressinit', 'sc_preparecheckoutperf',
'sc_buynowctatext', 'sc_buynowuiprod', 'sc_checkoutsalelegaltermsjp', 'sc_showooserrorforoneminute', 'sc_proratedrefunds', 'sc_entitlementcheckallitems', 'sc_indiaregsbanner', 'sc_checkoutentitlement', 'sc_rspv2', 'sc_focustrapforgiftthankyoupage', 'sc_hideneedhelp', 'sc_defaultshippingref', 'sc_uuid', 'sc_checkoutasyncpurchase', 'sc_nativeclientlinkredirect', 'sc_enablelegalrequirements', 'sc_expanded.purchasespinner', 'sc_valenciaupgrade', 'sc_enablezipplusfour', 'sc_giftingtelemetryfix', 'sc_handleentitlementerror', 'sc_alwayscartmuid', 'sc_sharedupgrade', 'sc_checkoutloadspinner', 'sc_xaaconversionexpirationdate', 'sc_helptypescript', 'sc_newdemandsandneedsstatement', 'sc_citizensoneallowed', 'sc_riskfatal', 'sc_renewtreatmenta', 'sc_trialtreatmenta', 'sc_cartzoomfix', 'sc_useofficeonlyinternalendpoint', 'sc_gotopurchase', 'sc_endallactivities', 'sc_headingheader', 'sc_flexsubs', 'sc_useanchorcomponent', 'sc_addbillingaddresstelemetry', 'sc_replacestoreappclient', 'sc_scenariotelemetryrefactor', 'sc_checkoutsmd', 'sc_scenariosupportupdate', 'sc_bankchallengecheckout', 'sc_addpaymenttelemetry', 'sc_railv2', 'sc_checkoutglobalpiadd', 'sc_reactcheckout', 'sc_xboxgotocart', 'sc_hidewarningevents', 'sc_xboxcomnosapi', 'sc_routebacktocartforoutofstock', 'sc_clientdebuginfo', 'sc_koreanlegalterms', 'sc_refactorprorate', 'sc_paymentoptionnotfound', 'sc_pidlflights', 'sc_fixcolorcontrastforrecommendeditems', 'sc_hideeditbuttonwhenediting', 'sc_enablekakaopay', 'sc_ordercheckoutfix', 'sc_xboxpmgrouping', 'sc_stickyfooter', 'sc_gotoredmrepl', 'sc_partnernametelemetry', 'sc_jpregionconversion', 'sc_checkoutorderedpv', 'sc_maxaddresslinelength', 'sc_componentexception', 'sc_buynowuipreload', 'sc_updatebillinginfo', 'sc_newshippingmethodtelemetry', 'sc_checkoutbannertelemetry', 'sc_learnmoreclcid', 'sc_satisfiedcheckout', 'sc_checkboxarialabel', 'sc_newlegaltextlayout', 'sc_newpagetitle', 'sc_prepaidcardsv3', 'sc_gamertaggifting', 'sc_checkoutargentinafee', 'sc_xboxcomasyncpurchase', 'sc_sameaddressdefault', 'sc_fixcolorcontrastforcheckout', 'sc_checkboxkg', 'sc_usebuynowbusinesslogic', 'sc_skippurchaseconfirm', 'sc_activitymonitorasyncpurchase', 'sc_shareddowngrade', 'sc_allowedpisenabled', 'sc_xboxoos', 'sc_eligibilityapi', 'sc_koreatransactionfeev1', 'sc_removesetpaymentmethod', 'sc_ordereditforincompletedata', 'sc_cppidlerror', 'sc_bankchallenge', 'sc_allowelo', 'sc_delayretry', 'sc_loadtestheadersenabled', 'sc_migrationforcitizenspay', 'sc_conversionblockederror', 'sc_allowpaysafecard', 'sc_purchasedblocked', 'sc_outofstock', 'sc_selectpmonaddfailure', 'sc_allowcustompifiltering', 'sc_errorpageviewfix', 'sc_windowsdevkitname', 'sc_xboxredirection', 'sc_usebuynowonlynonprodendpoint', 'sc_getmoreinfourl', 'sc_disablefilterforuserconsent', 'sc_suppressrecoitem', 'sc_dcccattwo', 'sc_hipercard', 'sc_resellerdetail', 'sc_fixpidladdpisuccess', 'sc_xdlshipbuffer', 'sc_allowverve', 'sc_inlinetempfix', 'sc_ineligibletostate', 'sc_greenshipping', 'sc_trackinitialcheckoutload', 'sc_creditcardpurge', 'sc_showlegalstringforproducttypepass', 'sc_newduplicatesubserror', 'sc_xboxgamepad', 'sc_xboxspinner', 'sc_xboxclosebutton', 'sc_xboxuiexp', 'sc_disabledefaultstyles', 'sc_gamertaggifting']
purchaseFlights = ['sc_appendconversiontype', 'sc_showvalidpis', 'sc_scdstextdirection', 'sc_optimizecheckoutload', 'sc_purchasedblockedby', 'sc_passthroughculture', 'sc_showcanceldisclaimerdefaultv1', 'sc_redirecttosignin', 'sc_paymentpickeritem', 'sc_cleanreducercode', 'sc_dimealipaystylingfix', 'sc_promocode', 'sc_onedrivedowngrade', 'sc_newooslogiconcart', 'sc_optionalcatalogclienttype', 'sc_klarna', 'sc_hidecontactcheckbox', 'sc_preparecheckoutrefactor', 'sc_checkoutklarna', 'sc_currencyformattingpkg', 'sc_fullpageredirectionforasyncpi', 'sc_xaaconversionerror', 'sc_promocodefeature-web-desktop', 'sc_eligibilityproducts', 'sc_disabledpaymentoption',
'sc_enablecartcreationerrorparsing', 'sc_purchaseblock', 'sc_returnoospsatocart', 'sc_dynamicseligibility', 'sc_usebuynowonlyinternalendpoint', 'sc_removemoreless', 'sc_renewalsubscriptionselector', 'sc_hidexdledd', 'sc_militaryshippingurl', 'sc_xboxdualleaf', 'sc_japanlegalterms', 'sc_multiplesubscriptions', 'sc_loweroriginalprice', 'sc_xaatovalenciastring', 'sc_cannotbuywarrantyalone', 'sc_showminimalfooteroncheckout', 'sc_checkoutdowngrade', 'sc_checkoutcontainsiaps', 'sc_localizedtax', 'sc_officescds', 'sc_disableupgradetrycheckout', 'sc_extendPageTagToOverride', 'sc_checkoutscenariotelemetry', 'sc_skipselectpi', 'sc_allowmpesapi', 'sc_purchasestatusmessage', 'sc_storetermslink', 'sc_postorderinfolineitemmessage', 'sc_addpaymentfingerprinttagging', 'sc_shippingallowlist', 'sc_emptyresultcheck', 'sc_dualleaf', 'sc_riskyxtoken', 'sc_abandonedretry', 'sc_testflightbuynow', 'sc_addshippingmethodtelemetry', 'sc_leaficons', 'sc_newspinneroverlay', 'sc_paymentinstrumenttypeandfamily', 'sc_addsitename', 'sc_disallowalipayforcheckout', 'sc_checkoutsignintelemetry', 'sc_prominenteddchange', 'sc_disableshippingaddressinit', 'sc_preparecheckoutperf',
'sc_buynowctatext', 'sc_buynowuiprod', 'sc_checkoutsalelegaltermsjp', 'sc_showooserrorforoneminute', 'sc_proratedrefunds', 'sc_entitlementcheckallitems', 'sc_indiaregsbanner', 'sc_checkoutentitlement', 'sc_rspv2', 'sc_focustrapforgiftthankyoupage', 'sc_hideneedhelp', 'sc_defaultshippingref', 'sc_uuid', 'sc_checkoutasyncpurchase', 'sc_nativeclientlinkredirect', 'sc_enablelegalrequirements', 'sc_expanded.purchasespinner', 'sc_valenciaupgrade', 'sc_enablezipplusfour', 'sc_giftingtelemetryfix', 'sc_handleentitlementerror', 'sc_alwayscartmuid', 'sc_sharedupgrade', 'sc_checkoutloadspinner', 'sc_xaaconversionexpirationdate', 'sc_helptypescript', 'sc_newdemandsandneedsstatement', 'sc_citizensoneallowed', 'sc_riskfatal', 'sc_renewtreatmenta', 'sc_trialtreatmenta', 'sc_cartzoomfix', 'sc_useofficeonlyinternalendpoint', 'sc_gotopurchase', 'sc_endallactivities', 'sc_headingheader', 'sc_flexsubs', 'sc_useanchorcomponent', 'sc_addbillingaddresstelemetry', 'sc_replacestoreappclient', 'sc_scenariotelemetryrefactor', 'sc_checkoutsmd', 'sc_scenariosupportupdate', 'sc_bankchallengecheckout', 'sc_addpaymenttelemetry', 'sc_railv2', 'sc_checkoutglobalpiadd', 'sc_reactcheckout', 'sc_xboxgotocart', 'sc_hidewarningevents', 'sc_xboxcomnosapi', 'sc_routebacktocartforoutofstock', 'sc_clientdebuginfo', 'sc_koreanlegalterms', 'sc_refactorprorate', 'sc_paymentoptionnotfound', 'sc_pidlflights', 'sc_fixcolorcontrastforrecommendeditems', 'sc_hideeditbuttonwhenediting', 'sc_enablekakaopay', 'sc_ordercheckoutfix', 'sc_xboxpmgrouping', 'sc_stickyfooter', 'sc_gotoredmrepl', 'sc_partnernametelemetry', 'sc_jpregionconversion', 'sc_checkoutorderedpv', 'sc_maxaddresslinelength', 'sc_componentexception', 'sc_buynowuipreload', 'sc_updatebillinginfo', 'sc_newshippingmethodtelemetry', 'sc_checkoutbannertelemetry', 'sc_learnmoreclcid', 'sc_satisfiedcheckout', 'sc_checkboxarialabel', 'sc_newlegaltextlayout', 'sc_newpagetitle', 'sc_prepaidcardsv3', 'sc_gamertaggifting', 'sc_checkoutargentinafee', 'sc_xboxcomasyncpurchase', 'sc_sameaddressdefault', 'sc_fixcolorcontrastforcheckout', 'sc_checkboxkg', 'sc_usebuynowbusinesslogic', 'sc_skippurchaseconfirm', 'sc_activitymonitorasyncpurchase', 'sc_shareddowngrade', 'sc_allowedpisenabled', 'sc_xboxoos', 'sc_eligibilityapi', 'sc_koreatransactionfeev1', 'sc_removesetpaymentmethod', 'sc_ordereditforincompletedata', 'sc_cppidlerror', 'sc_bankchallenge', 'sc_allowelo', 'sc_delayretry', 'sc_loadtestheadersenabled', 'sc_migrationforcitizenspay', 'sc_conversionblockederror', 'sc_allowpaysafecard', 'sc_purchasedblocked', 'sc_outofstock', 'sc_selectpmonaddfailure', 'sc_allowcustompifiltering', 'sc_errorpageviewfix', 'sc_windowsdevkitname', 'sc_xboxredirection', 'sc_usebuynowonlynonprodendpoint', 'sc_getmoreinfourl', 'sc_disablefilterforuserconsent', 'sc_suppressrecoitem', 'sc_dcccattwo', 'sc_hipercard', 'sc_resellerdetail', 'sc_fixpidladdpisuccess', 'sc_xdlshipbuffer', 'sc_allowverve', 'sc_inlinetempfix', 'sc_ineligibletostate', 'sc_greenshipping', 'sc_trackinitialcheckoutload', 'sc_creditcardpurge', 'sc_showlegalstringforproducttypepass', 'sc_newduplicatesubserror', 'sc_xboxgamepad', 'sc_xboxspinner', 'sc_xboxclosebutton', 'sc_xboxuiexp', 'sc_disabledefaultstyles', 'sc_gamertaggifting']
country_sm = locale.split("-")[1].lower()

def generate_permission_data(data:str, secret:str):
    time = int(te.time() * 1000)
    timeframe = int(time - (time % 36000))
    return {
    "pxmac": hmac.new(secret.encode('utf-8'), msg=f"PI|{data}|{timeframe}".encode('utf-8'), digestmod=hashlib.sha256).hexdigest().upper(),
    "keyToken": str(base64.b64encode(secret.encode('utf-8'))),
    "data": str(base64.b64encode(data.encode('utf-8')))
  } 
def db64(data, altchars=b'+/'):
        if len(data) % 4 and '=' not in data:
            data += '='* (4 - len(data) % 4)
        return base64.b64decode(data, altchars)
def sprint(content, status: str="c") -> None:
    thread_lock.acquire()
    if status=="y":
        colour = Fore.YELLOW
    elif status=="c":
        colour = Fore.CYAN
    elif status=="r":
        colour = Fore.RED
    elif status=="new":
        colour = Fore.LIGHTYELLOW_EX
        thread_lock.acquire()
    sys.stdout.write(
            f"{colour}{content}"
            + "\n"
            + Fore.RESET
        )    

    thread_lock.release()
def remove_content(filename: str, delete_line: str) -> None:
        thread_lock.acquire()
        with open(filename, "r+") as io:
            content = io.readlines()
            io.seek(0)
            for line in content:
                if not (delete_line in line):
                    io.write(line)
            io.truncate()
        thread_lock.release()
def getRandomLetters(len : int):
    return ''.join(random.choices(string.ascii_uppercase,k=len))

def generateHexStr(len: int):
    return ''.join(random.choices('0123456789abcdef', k=len))

def getRandomInt(len : int):
    return ''.join(random.choices(string.digits,k=len))


def main(ms_creds : str ):
    s = requests.session()
    if not proxies=="":
        s.proxies = {"https":proxies}
    email = ms_creds.split("|")[0]
    password = ms_creds.split("|")[1]

    s = requests.session()
    if not proxies=="":
        s.proxies = {"https":proxies}
    email = ms_creds.split("|")[0]
    password = ms_creds.split("|")[1]
    
    headers = {

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'identity',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
}

    while True:
        try:
            response = s.get('https://login.live.com/ppsecure/post.srf', headers=headers,timeout=20).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(str(e),"r")
            return
    try:
        ppft = response.split(''''<input type="hidden" name="PPFT" id="i0327" value="''')[1].split('"')[0]
        log_url = response.split(",urlPost:'")[1].split("'")[0]
    except:
        print(Fore.RED + '[ - ] Proxy Issue')
        return
    log_data = f'i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={ppft}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i19=449894'
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://login.live.com',
    'Referer': 'https://login.live.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
            }  
    while True:
        try:
            response = s.post(log_url,timeout=20,data=log_data,headers=headers).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return


    try:
        ppft2 = re.findall("sFT:'(.+?(?=\'))", response)[0],
        url_log2 = re.findall("urlPost:'(.+?(?=\'))", response)[0]
    except:
        print(Fore.RED+ '[ - ] Invalid MS Account')
        remove_content("accounts.txt",ms_creds)
        return


    log_data2 = {
    "LoginOptions": "3",
    "type": "28",
    "ctx": "",
    "hpgrequestid": "",
    "PPFT": ppft2,
    "i19": "19130"
}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://login.live.com',
        'Referer': log_url,
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua,
    }
    while True:
        try:
            midAuth2 = s.post(url_log2,timeout=20,data=log_data2,headers=headers).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return
    heads = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
}
    while True:
        try:
            response = s.get("https://account.xbox.com/",timeout=20,headers=heads).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return
    try:
        xbox_json = {
"fmHF": response.split('id="fmHF" action="')[1].split('"')[0],
"pprid": response.split('id="pprid" value="')[1].split('"')[0],
"nap": response.split('id="NAP" value="')[1].split('"')[0],
"anon": response.split('id="ANON" value="')[1].split('"')[0],
"t": response.split('id="t" value="')[1].split('"')[0]} 
    except:
        print(Fore.YELLOW + ' [ - ] Account Issue : TrustedState')
        return
    heads = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://login.live.com',
    'Referer': 'https://login.live.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
}
    while True:
        try:
            verify_token = s.post(xbox_json['fmHF'],timeout=20, headers={
        'Content-Type': 'application/x-www-form-urlencoded',
    },data={
        "pprid": xbox_json['pprid'],
        "NAP": xbox_json['nap'],
        "ANON": xbox_json['anon'],
        "t": xbox_json['t']
    }).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return
    

    reqVerifytoken = verify_token.split('name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
    heads={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://account.xbox.com',
    'Referer': xbox_json['fmHF'],
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': ua,
    'X-Requested-With': 'XMLHttpRequest',
    '__RequestVerificationToken': reqVerifytoken,
}
    while True:
        try:
            make_acc = s.post("https://account.xbox.com/en-us/xbox/account/api/v1/accountscreation/CreateXboxLiveAccount",timeout=20, headers=heads,data={
        "partnerOptInChoice": "false",
        "msftOptInChoice": "false",
        "isChild": "true",
        "returnUrl": "https://www.xbox.com/en-US/?lc=1033"
    })
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return
    if not make_acc.ok:
        print(Fore.YELLOW + '[ - ] Failed to create xbox profile')
        return
    heads = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
}
    while True:
        try:
            response = s.get(f"https://account.xbox.com/{locale}/auth/getTokensSilently?rp=http://xboxlive.com,http://mp.microsoft.com/,http://gssv.xboxlive.com/,rp://gswp.xboxlive.com/,http://sisu.xboxlive.com/",timeout=20).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return
    try:
        rel = response.split('"http://mp.microsoft.com/":{')[1].split('},')[0]
        json_obj = json.loads("{"+rel+"}")
        xbl_auth = "XBL3.0 x=" + json_obj['userHash'] + ";" + json_obj['token']
        xbl_auth2 = str({"XToken":xbl_auth})
    except:
        print(Fore.RED + '[ - ] Failed to get Xbox Live Auth","y")')
        remove_content("accounts.txt",ms_creds)

colorama.init()
thread_count = int(input(Fore.CYAN+" [ > ] Threads : "))

if __name__=="__main__":
    emails_list = open("accounts.txt").read().splitlines()

    while len(emails_list)  > 0:
        try:
            local_threads = []
            for x in range(thread_count):

                try:
                    email = emails_list[0]
                except:
                    try:
                        emails_list = open("accounts.txt").read().splitlines()
                        email = emails_list[0]
                    except:
                        break

                start_thread = threading.Thread(
                    target=main,
                    args=(
                        email,
                    ),
                )
                local_threads.append(start_thread)
                start_thread.start()

                try:
                    emails_list.pop(0)
                except:
                    pass

            for thread in local_threads:
                thread.join()

        except IndexError:
            break
        except:
            pass

print(Fore.GREEN +'[ + ] Successfully Completed Task')
exit(0)