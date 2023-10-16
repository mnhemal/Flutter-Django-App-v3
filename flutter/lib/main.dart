////Building a Register App with Flutter and Django

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Register App',
      theme: ThemeData(
        primarySwatch: Colors.cyan,
      ),
      home: const MyRegisterApp(title: 'Register App'),
    );
  }
}

class MyRegisterApp extends StatefulWidget {
  const MyRegisterApp({Key? key, required String title}) : super(key: key);

  @override
  State<MyRegisterApp> createState() => _MyRegisterAppState();
}

class _MyRegisterAppState extends State<MyRegisterApp> {
  final _formKey = GlobalKey<FormState>();
  final _scaffoldKey = GlobalKey<ScaffoldState>();
  final _usernameController = TextEditingController();
  final _firstnameController = TextEditingController();
  final _lastnameController = TextEditingController();
  final _passwordController = TextEditingController();
  final _emailController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      key: _scaffoldKey,
      appBar: AppBar(
        title: const Text('Signup to Register App'),
      ),
      body: Form(
        key: _formKey,
        child: ListView(
          padding: const EdgeInsets.symmetric(horizontal: 16.0),
          children: <Widget>[
            const SizedBox(height: 80.0),
            TextFormField(
              controller: _firstnameController,
              decoration: const InputDecoration(
                labelText: 'first name',
              ),
              validator: (value) {
                if (value!.isEmpty) {
                  return 'Please enter some text';
                }
                return null;
              },
            ),
            const SizedBox(height: 12.0),
            TextFormField(
              controller: _lastnameController,
              decoration: const InputDecoration(
                labelText: 'last name',
              ),
              validator: (value) {
                if (value!.isEmpty) {
                  return 'Please enter some text';
                }
                return null;
              },
            ),
             const SizedBox(height: 12.0),
            TextFormField(
              controller: _usernameController,
              decoration: const InputDecoration(
                labelText: 'Username',
              ),
              validator: (value) {
                if (value!.isEmpty) {
                  return 'Please enter some text';
                }
                return null;
              },
            ),
            const SizedBox(height: 12.0),
            TextFormField(
              controller: _emailController,
              decoration: const InputDecoration(
                labelText: 'Email',
              ),
              validator: (value) {
                if (value!.isEmpty) {
                  return 'Please enter some text';
                }
                return null;
              },
            ),
            const SizedBox(height: 12.0),
            TextFormField(
              controller: _passwordController,
              decoration: const InputDecoration(
                labelText: 'Password',
              ),
              obscureText: true,
              validator: (value) {
                if (value!.isEmpty) {
                  return 'Please enter some text';
                }
                return null;
              },
            ),
            const SizedBox(height: 12.0),
            SizedBox(
              height: 44.0,
              child: ElevatedButton(
                  child: const Text('Signup'),
                  onPressed: () async {
                    if (_formKey.currentState!.validate()) {
                      await http.post(Uri.parse('http://127.0.0.1:8000/v1/api/users/users/'),
                          body: {
                            'username': _usernameController.text,
                            'email': _emailController.text,
                            'password_hash': _passwordController.text,
                            'first_name': _firstnameController.text,
                            'last_name': _lastnameController.text,
                            
                          }).then((response) {
                        if (response.statusCode == 201) {
                          //msg pop up
                          ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(content: Text('Signup Success')));
                        } else {
                          ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(content: Text('Signup Failed')));
                        }
                      });
                    }
                  }),
            ),
          ],
        ),
      ),
    );
  }
}