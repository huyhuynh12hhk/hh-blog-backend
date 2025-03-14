package com.hhk.identity.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.hhk.identity.entities.Permission;

@Repository
public interface PermissionRepository extends JpaRepository<Permission, String> {}
