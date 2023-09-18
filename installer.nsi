!define MyAppName "Puzzle Box"
!define MyAppVersion "1.0"
!define MyAppPublisher "E. =D"
!define OutputDir "."
!define OutPutFileName "PuzzleBoxInstaller"
!define INSTALLER_ICON "C:\Users\Eck\Desktop\Projetos\puzzlebox\icone_small.ico"

Outfile "${OutPutFileName}.exe"
SetCompressor /SOLID lzma
Name "${MyAppName} ${MyAppVersion}"
Icon "${INSTALLER_ICON}"
InstallDir "$PROGRAMFILES\${MyAppName}"

Section "MainSection" SEC01
    SetOutPath $INSTDIR
    
    File "C:\Users\Eck\Desktop\Projetos\puzzlebox\dist\Puzzle_Box.exe"
    
    # Adicione o ícone ao instalador e copie-o para o diretório de instalação
    File "${INSTALLER_ICON}"
    
    CreateDirectory "$INSTDIR\MyApp"
    CreateShortCut "$SMPROGRAMS\${MyAppName}\${MyAppName}.lnk" "$INSTDIR\Puzzle_Box.exe" "" "${INSTALLER_ICON}" 0
    CreateShortCut "$DESKTOP\${MyAppName}.lnk" "$INSTDIR\Puzzle_Box.exe" "" "${INSTALLER_ICON}" 0
SectionEnd

Section "Uninstall"
    Delete "$INSTDIR\Puzzle_Box.exe"
    
    # (Opcional) Exclua o ícone durante a desinstalação
    Delete "$INSTDIR\icone_small.ico"
    
    RMDir $INSTDIR
    Delete "$SMPROGRAMS\Puzzle Box\Puzzle Box.lnk"
    RMDir "$SMPROGRAMS\Puzzle Box"
    Delete "$DESKTOP\${MyAppName}.lnk"
SectionEnd
