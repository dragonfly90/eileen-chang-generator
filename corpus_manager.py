import os
import random
import glob
from typing import List

class CorpusManager:
    """
    Manages Eileen Chang's novel corpus for style reference.
    
    Usage:
    1. The manager will create a sample corpus file on first run
    2. To add more texts, simply place .txt files in the 'corpus/' directory
    3. All .txt files will be automatically loaded and used for style reference
    
    Recommended: Add full texts of Eileen Chang's novels like:
    - 倾城之恋 (Love in a Fallen City)
    - 金锁记 (The Golden Cangue)
    - 红玫瑰与白玫瑰 (Red Rose, White Rose)
    - 半生缘 (Half a Lifelong Romance)
    """
    
    def __init__(self, corpus_dir: str = "corpus"):
        self.corpus_dir = corpus_dir
        self.texts = []
        if not os.path.exists(self.corpus_dir):
            os.makedirs(self.corpus_dir)

    def download_corpus(self):
        """
        Creates sample corpus files if none exist.
        
        Note: Due to copyright restrictions, automatic downloading is not available.
        Users should manually add .txt files to the corpus directory.
        """
        existing_files = glob.glob(os.path.join(self.corpus_dir, "*.txt"))
        
        if existing_files:
            print(f"Found {len(existing_files)} existing corpus files.")
            return
        
        print("No corpus files found. Creating sample file with Eileen Chang excerpts...")
        self._create_sample_file()
        print("\nTo improve style emulation, add more .txt files to the 'corpus/' directory.")

    def _create_sample_file(self):
        """Creates a sample file with authentic Eileen Chang excerpts."""
        sample_text = """胡琴咿咿哑哑拉着，在万盏灯的夜晚，拉过来又拉过去，说不尽的苍凉的故事——不问也罢！

风从窗子里进来，对面挂着的回文雕漆长镜被吹得摇摇晃晃，磕托磕托敲着墙。七巧双手按住了镜子。镜子里反映着的翠竹帘子和一副金绿山水屏条依旧在风中来回荡漾着，望久了，便有一种晕船的感觉。再定睛看时，翠竹帘子已经褪了色，金绿山水换了一张她丈夫的遗像，镜子里的人也老了十年。

那是个潮湿的下午，像一团拧不干的湿布。

她穿着一件苹果绿软缎旗袍，那绿色绿得流油，像是一只刚切开的青苹果。

三十年前的月亮早已沉了下去，三十年前的人也死了，然而三十年前的故事还没完——完不了。

年轻的人想着三十年前的月亮该是铜钱大的一个红黄的湿晕，像朵云轩信笺上落了一滴泪珠，陈旧而迷糊。老年人回忆中的三十年前的月亮是欢愉的，比眼前的月亮大、圆、白；然而隔着三十年的辛苦路望回看，再好的月色也不免带点凄凉。

她那平扁而尖利的喉咙四面割着人像剃刀片。

生在这世上，没有一样感情不是千疮百孔的。

也许每一个男子全都有过这样的两个女人，至少两个。娶了红玫瑰，久而久之，红的变了墙上的一抹蚊子血，白的还是"床前明月光"；娶了白玫瑰，白的便是衣服上沾的一粒饭黏子，红的却是心口上一颗朱砂痣。

对于三十岁以后的人来说，十年八年不过是指缝间的事，而对于年轻人而言，三年五年就可以是一生一世。

我要你知道，在这个世界上总有一个人是等着你的，不管在什么时候，不管在什么地方，反正你知道，总有这么个人。

于千万人之中遇见你所要遇见的人，于千万年之中，时间的无涯的荒野里，没有早一步，也没有晚一步，刚巧赶上了，那也没有别的话可说，惟有轻轻地问一声："噢，你也在这里吗？"

她的眼睛像两只黑葡萄，又圆又亮，然而是死的。

他觉得她的手像一只小鸟，轻轻地停在他的手上。

月光像流水一般，静静地泻在这一片叶子和花上。薄薄的青雾浮起在荷塘里。叶子和花仿佛在牛乳中洗过一样；又像笼着轻纱的梦。

上海人是传统的中国人加上近代高压生活的磨练。新旧文化种种畸形产物的交流，结果也许是不甚健康的，但是这里有一种奇异的智慧。

笑，全世界便与你同声笑，哭，你便独自哭。

因为懂得，所以慈悲。

长的是磨难，短的是人生。

你如果认识从前的我，也许会原谅现在的我。

我以为爱情可以填满人生的遗憾。然而，制造更多遗憾的，却偏偏是爱情。

有一天我们的文明，不论是升华还是浮华，都要成为过去。然而现在还是清如水明如镜的秋天，我应当是快乐的。"""
        
        filename = os.path.join(self.corpus_dir, "eileen_chang_excerpts.txt")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(sample_text)
        print(f"Created sample corpus file: {filename}")

    def load_corpus(self):
        """Loads all .txt files from the corpus directory."""
        self.texts = []
        files = glob.glob(os.path.join(self.corpus_dir, "*.txt"))
        
        if not files:
            print("Warning: No corpus files found. Run download_corpus() first.")
            return
            
        for file in files:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.strip():  # Only add non-empty files
                        self.texts.append(content)
                        print(f"Loaded: {os.path.basename(file)} ({len(content)} chars)")
            except Exception as e:
                print(f"Error reading {file}: {e}")
        
        print(f"\nTotal: Loaded {len(self.texts)} text file(s) from corpus.")

    def get_random_snippet(self, length: int = 500) -> str:
        """Returns a random snippet from the loaded corpus."""
        if not self.texts:
            return ""
        
        text = random.choice(self.texts)
        if len(text) <= length:
            return text
        
        start = random.randint(0, len(text) - length)
        return text[start:start + length]

if __name__ == "__main__":
    cm = CorpusManager()
    cm.download_corpus()
    cm.load_corpus()
    if cm.texts:
        print(f"\nRandom snippet:\n{cm.get_random_snippet(200)}")
