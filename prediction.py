import sys
import fasttext as ft
import MeCab

class predict:

    def __init__(self):
        # モデル読み込み
        self.classifier = ft.load_model('negaposi2.bin')


    def get_surfaces(self, content):
        """
        文書を分かち書き
        """
        tagger = MeCab.Tagger('')
        tagger.parse('')
        surfaces = []
        node = tagger.parseToNode(content)

        while node:
            surfaces.append(node.surface)
            node = node.next

        return surfaces 


    def tweet_class(self, content):
        """
        ツイートを解析して分類を行う
        """
        words = " ".join(self.get_surfaces(content))
        estimate = self.classifier.predict_proba([words], k=2)[0][0]

        if estimate[0] == "__label__1,":
            print('ネガティブ', estimate[1])
        elif estimate[0] == "__label__2,":
            print('ポジティブ', estimate[1])
      ##  elif estimate[0] == "__label__3,":
          ##  print('暮らし系', estimate[1])


if __name__ == '__main__':
    pre = predict()
    pre.tweet_class("".join(sys.argv[1:]))
