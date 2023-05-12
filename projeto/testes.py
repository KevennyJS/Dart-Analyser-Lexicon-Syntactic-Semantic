kev_codes = """
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import '../../../domain/entity/login_response_entity.dart';

const KEY_SESSION_TOKEN = 'SESSION_TOKEN';
const keySessionUser = 'SESSION_USER';

abstract class AuthLocalDataSource {
  Future<LoginResponseEntity> getCurrentUser();

  Future<bool> setCurrentUser(LoginResponseEntity user);

  Future<bool> setToken(String token);

  Future<String> getToken();

  Future<bool> cleanToken();
}

class AuthLocalDatasourceImpl implements AuthLocalDataSource {
  const AuthLocalDatasourceImpl();

  @override
  Future<LoginResponseEntity> getCurrentUser() async {
    final sharedPreferences = await SharedPreferences.getInstance();

    final userJsonString = sharedPreferences.getString(
      keySessionUser,
    );

    if (userJsonString == null) throw Exception("Não há escolas dispoíveis");

    final result = LoginResponseEntity.fromMap(jsonDecode(userJsonString));

    return result;
  }

  @override
  Future<bool> setCurrentUser(LoginResponseEntity user) async {
    final sharedPreferences = await SharedPreferences.getInstance();

    final userJson = jsonEncode(user.toMap());
    print("Salvando usuário: $userJson");
    final result = sharedPreferences.setString(
      keySessionUser,
      userJson,
    );

    return result;
  }

  @override
  Future<String> getToken() async {
    final sharedPreferences = await SharedPreferences.getInstance();

    final schoolYearString = sharedPreferences.getString(
      KEY_SESSION_TOKEN,
    );

    if (schoolYearString == null) {
      throw Exception("Não há TOKEN disponível");
    }

    return schoolYearString;
  }

  @override
  Future<bool> setToken(String token) async {
    final sharedPreferences = await SharedPreferences.getInstance();

    final result = sharedPreferences.setString(
      KEY_SESSION_TOKEN,
      token,
    );

    return result;
  }

  @override
  Future<bool> cleanToken() async {
    final sharedPreferences = await SharedPreferences.getInstance();

    final result = sharedPreferences.remove(KEY_SESSION_TOKEN);

    return result;
  }
}
"""

vere_codes2 = """void main(){}"""

#FOR LPAREN tiposassign INTERROGATION SEMI_COLON exp INTERROGATION SEMI_COLON exp INTERROGATION  RPAREN body
  # for(int a = 2;exp?;){

  # }
vere_codes = """
void testando(int a){
  
}

void main (){
  int a = 0;
  int b = 8;
  int c = 0;
  c = c + a;
  c = c - 8;
  somaDois();
  if(c == 1){
    
  }
  else if(c >= 2){

  }
  else if(c is a){
    
  }
  for(int i = 0;;){

  }
  for(int a in lista){

  }
}

void somaDois(){
  int b = 2 + 1;
}

"""