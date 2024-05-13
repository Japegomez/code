import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { UserSession } from '../interfaces/user';

@Injectable({
  providedIn: 'root'
})
export class APIService {
  user!: UserSession;
  constructor(private http: HttpClient ) { 
  }
  getSessionConfig(): Observable<UserSession> {
    return this.http.get<UserSession>('http://localhost:5000/api/v1/config');
  }

  sendLabConfig(typeCircuit: string, subtype: string) {
    return this.http.post('localhost:5000/api/v1/lab/', {typeCircuit, subtype});
  }


}

