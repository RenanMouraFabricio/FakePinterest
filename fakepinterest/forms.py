from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Entrar")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Usuário inexistente, crie uma conta para continuar.")
class FormCriarConta(FlaskForm):
    username = StringField("Nome", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(8, 16)])
    confirmacao_senha = PasswordField("Repetir Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado, utilize outro e-mail para criar sua conta ou faça login para continuar.")


class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")