import os
import re
from gtts import gTTS


class VoiceProcess():
    def __init__(self, guild_dir: str):
        self.__guild_dir = guild_dir
        self.__voice_output_dir = os.path.join(self.__guild_dir, 'command_parrot/voice')
        self.__output_file = os.path.join(self.__voice_output_dir, 'voice_line.mp3')
        
    
    '''
    # process_check
    
    ## 備考
    > 処理前に行うライセンスの有無の確認で対象のギルドフォルダがあるか確認するため、ギルドフォルダの確認は不要
    
    [処理を行わないケース]
    1. 作成済みの音声ファイルがある場合(読み上げ中の場合/削除に失敗した場合)
    2. 
    '''
    def process_check(self):
        
        if not os.path.isdir(self.__guild_dir):
            return False
        
        # 出力先がない場合は作成する。
        if not os.path.isdir(self.__voice_output_dir):
            os.mkdir(self.__voice_output_dir)

        # 音声ファイルを再生中じゃない場合、上書きしないような使用になったため確認不要
        # if os.path.isfile(self.__output_file):
        #     return False 
        
        return True

    def create(self, context: str):        
        # 括弧内の文字を削除する(re.subの第2引数は''で固定すること。変な文字を入れるとttsがエラーを吐く)
        mute_pattern = '(\(.+?\))|(\（.+?\）)|(\[.+?\])|<@[0-9]{1,}>|<@&[0-9]{1,}>'
        input_text = re.sub(mute_pattern, '', context)
        regix_pattern = '(http?://[\w/:%#\$&\?\(\)~\.=\+\-]+)|(https?://[\w/:%#\$&\?\(\)~\.=\+\-]+)'
        test_to_read = re.sub(regix_pattern, '', input_text)

        if len(test_to_read) <= 32:
            text_to_read = test_to_read[0:32]
        else:
            text_to_read = '{0} .以下略'.format(test_to_read[0:32])
            
        if not text_to_read == '' or not text_to_read == None:        
            voice_file = gTTS(text=text_to_read, lang='ja')
            voice_file.save(self.__output_file)
        
            return self.__output_file
        else:
            return None

    # def delete(self):        
        
    #     if os.path.isfile(self.__output_file):
    #         os.remove(self.__output_file)    
            
            