*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username    newuser
    Set Password    password123
    Set Password Confirmation    password123
    Click    button >> text=Register
    Get Title    ==    Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username    ab
    Set Password    password123
    Set Password Confirmation    password123
    Click    button >> text=Register
    Register Should Fail With Message    Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username    newuser
    Set Password    short
    Set Password Confirmation    short
    Click    button >> text=Register
    Register Should Fail With Message    Password must be at least 8 characters long

Register With Username That Is Already In Use
    Set Username    kalle
    Set Password    password123
    Set Password Confirmation    password123
    Click    button >> text=Register
    Register Should Fail With Message    Username already exists

*** Keywords ***

Set Username
    [Arguments]    ${username}
    Fill Text    id=username    ${username}

Set Password
    [Arguments]    ${password}
    Fill Secret    id=password    $password

Set Password Confirmation
    [Arguments]    ${password}
    Fill Secret    id=password_confirmation    $password

Register Should Fail With Message
    [Arguments]    ${message}
    Get Title    ==    Register
    Get Text    body    *=    ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To    ${REGISTER_URL}