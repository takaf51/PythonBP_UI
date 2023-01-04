import unreal

print('Tools were successfully loaded')


def addPreSuffixOnSelectedAssets(prefix, suffix):
    EUL = unreal.EditorUtilityLibrary
    assetDatas = EUL.get_selected_asset_data()
    for data in assetDatas:
        newName = unreal.StringLibrary.build_string_name('', prefix, data.asset_name, suffix)
        EUL.rename_asset(data.get_asset(), newName)


def getTextureCompressionSettingsAsList():
    return list(map(lambda setting: setting.name, unreal.TextureCompressionSettings))


def getSelectedAssetsByClass(classType):
    EUL = unreal.EditorUtilityLibrary
    assets = EUL.get_selected_asset_data()
    filteredAssets = []
    for asset in assets:
        if asset.get_class().get_name() == classType:
            filteredAssets.append(asset)
    return filteredAssets


def getSelectedAssetsNameByClass(classType):
    EUL = unreal.EditorUtilityLibrary
    assets = EUL.get_selected_asset_data()
    filteredAssetNames = []
    for asset in assets:
        if asset.get_class().get_name() == classType:
            filteredAssetNames.append(asset.asset_name)
    return filteredAssetNames


def saveAsset(assetName):
    EAL = unreal.EditorAssetLibrary
    if len(assetName) != 0:
        try:
            EAL.save_asset(assetName)
        except TypeError as e:
            print(f'Save Asset Error : {e}')
            return False
        else:
            print('saved')
            return True


def changeTextureCompressionSetting(Texture2Ds, newSetting):
    SL = unreal.StringLibrary
    successCount = 0
    try:
        compressionSetting = getattr(unreal.TextureCompressionSettings, newSetting)
    except AttributeError as e:
        print(f'Catch Attribute Error: {e}')
        return 0
    except ValueError as e:
        print(f'Catch Value Error: {e}')
        return 0
    for Texture2D in Texture2Ds:
        try:
            Texture2D.get_asset().set_editor_property('compression_settings', compressionSetting)
            path = SL.build_string_name('', '', Texture2D.package_name, '')
            saveAsset(path)
            successCount += 1
        except TypeError:
            print("Setting and Save Error")
            pass
    return successCount
