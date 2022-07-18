!git clone https://github.com/gutfeeling/word_forms.git
!pip install unipath

# from word_forms.word_forms.word_forms import get_word_forms

# if __name__ == "__main__":

#   word = "hum"
#   print(get_word_forms(word)['v'])

!pip install lm-scorer
!pip install torch
import torch
from lm_scorer.models.auto import AutoLMScorer as LMScorer

def get_score(scorer, sentence):
  return scorer.sentence_score(sentence, log=True)

def get_best_question(scorer, templates):
  scored_templates = {}

  for template in templates:
    scored_templates[template] = get_score(scorer, template)
  
  return max(scored_templates, key=scored_templates.get)

def transform(template, parent_of_node, sentence):

    #storing the word from the parent node into the variable prefix
    elements = parent_of_node.split(sep=" ")
    value = elements[3]
    if(value[-1]==")"):
        prefix = value[:-1]
    else:
        prefix = value
    if "-" in prefix:
        index = prefix.find("-")
        prefix = prefix[:index]

    #creating all possible questions with forms of prefix  
    from word_forms.word_forms.word_forms import get_word_forms

    list_of_word_forms = get_word_forms(prefix)['v']
    list_of_questions = []
    for form in list_of_word_forms:
        question=template.replace('*', form)
        list_of_questions.append(question)

      # Load model to cpu or cuda
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    batch_size = 1
    scorer = LMScorer.from_pretrained("gpt2", device=device, batch_size=batch_size)

    templates = list_of_questions

    print(templates)

    #print(get_score(scorer, sent1))
    #print(get_score(scorer, sent2))
    print(get_best_question(scorer, templates))
        

#test parameters
templ = "Who *?"
parent_node = ":ARG1 (s / swallow-01"
sent = "In the book it said : ' Boa constrictors swallow their prey whole , without chewing it .'"

print(transform(templ, parent_node, sent))





















