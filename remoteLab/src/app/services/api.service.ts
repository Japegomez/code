import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, map, tap } from 'rxjs';
import { GetCameraResponse } from '../interfaces/camera';
import { GetMeasurementResponse } from '../interfaces/measurements';
import { GetSessionConfigResponse } from '../interfaces/sessionConfig';

@Injectable({
  providedIn: 'root'
})
export class APIService {
  sessionConfig?: GetSessionConfigResponse;
  measurements?: GetMeasurementResponse;
  camera?: GetCameraResponse;
  constructor(private http: HttpClient ) { 
  }
  getSessionConfig(): Observable<GetSessionConfigResponse> {
    return this.http.get<GetSessionConfigResponse>('http://pi:5000/api/v1/config', {
      withCredentials: true
    }).pipe(
      tap((data: GetSessionConfigResponse) => {
        this.sessionConfig = data;
      })
    ); 
  }

  runLabConfig(typeCircuit: string, subtype: number): Observable<GetMeasurementResponse> {
    const url = 'http://pi:5000/api/v1/lab';
    const body = {
      caso: typeCircuit,
      numero: subtype
    };
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      withCredentials: true
    };

    return this.http.post<GetMeasurementResponse>(url, body, options).pipe(
      tap((data: GetMeasurementResponse) => {
        this.measurements = data;
      })
    );
  }

  getImage(): Observable<{ id: string, image: Blob }> {
      return this.http.get('http://pi:5000/api/v1/image', { withCredentials:true, observe: 'response', responseType: 'blob' })
        .pipe(
          map(response => {
            const id = response.headers.get('Image-ID') || '';
            return { id, image: response.body as Blob };
          })
        );
      }
  logout() {
    return this.http.post('http://pi:5000/api/v1/logout',{},{ withCredentials: true });
  }
  
}

