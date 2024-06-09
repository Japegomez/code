import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { Router } from '@angular/router';
import { catchError, of } from 'rxjs';

export const unauthorizedInterceptor: HttpInterceptorFn = (req, next) => {
  const router = inject(Router);
  
  return next(req).pipe(catchError((err) => {
    if (err.status === 403) {
      router.navigate(['/unauthorized']);;
    }
    return of(err)
  }))
}

