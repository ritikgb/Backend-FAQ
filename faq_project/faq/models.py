from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi Translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali Translation

    def translate_text(self, text, target_lang):
        cache_key = f"translation_{text}_{target_lang}"
        translated_text = cache.get(cache_key)

        if not translated_text:
            translated_text = translator.translate(text, dest=target_lang).text
            cache.set(cache_key, translated_text, timeout=86400)  # Cache for 1 day

        return translated_text

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, "hi")
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, "bn")
        super().save(*args, **kwargs)

    def get_translated_question(self, lang="en"):
        translations = {
            "hi": self.question_hi,
            "bn": self.question_bn,
            "en": self.question
        }
        return translations.get(lang, self.question)

    def __str__(self):
        return self.question
